import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getQuestions, submitTest } from '../utils/api';
import Navbar from '../components/Navbar';
import LoadingSpinner from '../components/LoadingSpinner';

const TestPage = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [answers, setAnswers] = useState({});
  const [error, setError] = useState('');
  const [language, setLanguage] = useState(() => localStorage.getItem('testLanguage') || 'en');
  const [translating, setTranslating] = useState(false);

  useEffect(() => {
    fetchQuestions();
  }, []);

  const fetchQuestions = async () => {
    try {
      setLoading(true);
      // Fetch with Urdu to trigger backend translation
      const data = await getQuestions(user.role, 'ur');
      setQuestions(data.questions);
      setError('');
    } catch (error) {
      setError(error.response?.data?.error || 'Failed to load questions');
    } finally {
      setLoading(false);
    }
  };

  const handleLanguageChange = (newLanguage) => {
    if (newLanguage === language) return;
    localStorage.setItem('testLanguage', newLanguage);
    setLanguage(newLanguage);
  };

  const getDisplayText = (question, field) => {
    const urduField = `${field}_ur`;
    const enField = `${field}_en`;
    
    if (language === 'ur' && question[urduField]) {
      return question[urduField];
    }
    return question[enField] || question[field];
  };

  const handleAnswerSelect = (questionId, option) => {
    setAnswers({
      ...answers,
      [questionId]: option
    });
  };

  const handleSubmit = async () => {
    // Validate all questions are answered
    if (Object.keys(answers).length < questions.length) {
      alert('Please answer all questions before submitting');
      return;
    }

    setSubmitting(true);

    try {
      const result = await submitTest(answers);
      // Navigate to result page with data
      navigate('/result', { state: { result } });
    } catch (error) {
      setError(error.response?.data?.error || 'Failed to submit test');
      setSubmitting(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Loading your test questions..." />;
  }

  if (error && questions.length === 0) {
    return (
      <div className="min-h-screen bg-white">
        <Navbar />
        <div className="max-w-4xl mx-auto py-12 px-4">
          <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
            <div className="text-red-600 text-5xl mb-4">⚠️</div>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Error Loading Test</h2>
            <p className="text-gray-600 mb-6">{error}</p>
            <button
              onClick={() => navigate('/home')}
              className="px-6 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700"
            >
              Back to Home
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white">
      <Navbar />
      
      <div className="max-w-4xl mx-auto py-12 px-4">
        {/* Header */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-8">
          <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">
                {user?.role} Certification Test
              </h1>
              <p className="text-gray-600 mt-1">
                Answer all {questions.length} questions to complete the test
              </p>
            </div>
            <div className="flex flex-col md:items-end gap-4 md:gap-3 w-full md:w-auto">
              <div className="flex items-center justify-between md:justify-end gap-4">
                <div className="inline-flex rounded-full border border-primary-200 overflow-hidden">
                  <button
                    type="button"
                    onClick={() => handleLanguageChange('en')}
                    className={`px-4 py-2 text-sm font-semibold transition-colors ${
                      language === 'en'
                        ? 'bg-primary-600 text-white'
                        : 'bg-white text-primary-600 hover:bg-primary-50'
                    }`}
                  >
                    English
                  </button>
                  <button
                    type="button"
                    onClick={() => handleLanguageChange('ur')}
                    className={`px-4 py-2 text-sm font-semibold transition-colors ${
                      language === 'ur'
                        ? 'bg-primary-600 text-white'
                        : 'bg-white text-primary-600 hover:bg-primary-50'
                    }`}
                  >
                    اُردو
                  </button>
                </div>
                <span className="text-sm text-gray-500">
                  Questions shown in {language === 'ur' ? 'Urdu' : 'English'}
                </span>
              </div>
              <div className="text-right">
                <div className="text-3xl font-bold text-primary-600">
                  {Object.keys(answers).length}/{questions.length}
                </div>
                <div className="text-sm text-gray-600">Answered</div>
              </div>
            </div>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="mb-8">
          <div className="w-full bg-gray-200 rounded-full h-3">
            <div 
              className="bg-primary-600 h-3 rounded-full transition-all duration-300"
              style={{ width: `${(Object.keys(answers).length / questions.length) * 100}%` }}
            ></div>
          </div>
        </div>

        {/* Questions */}
        <div className="space-y-6">
          {questions.map((question, index) => (
            <div key={question.id} className="bg-white rounded-xl shadow-lg p-6">
              <div className="flex items-start mb-4">
                <div className="bg-primary-600 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-4 flex-shrink-0">
                  {index + 1}
                </div>
                <h3 className="text-lg font-semibold text-gray-900" style={{ direction: language === 'ur' ? 'rtl' : 'ltr' }}>
                  {getDisplayText(question, 'question_text')}
                </h3>
              </div>

              <div className="space-y-3 ml-12">
                {['A', 'B', 'C', 'D'].map((option) => (
                  <label
                    key={option}
                    className={`flex items-start p-4 border-2 rounded-lg cursor-pointer transition ${
                      answers[question.id] === option
                        ? 'border-primary-600 bg-primary-50'
                        : 'border-gray-200 hover:border-primary-300'
                    }`}
                  >
                    <input
                      type="radio"
                      name={`question-${question.id}`}
                      value={option}
                      checked={answers[question.id] === option}
                      onChange={() => handleAnswerSelect(question.id, option)}
                      className="mt-1 mr-3"
                    />
                    <div className="flex-1">
                      <div className="font-semibold text-gray-700 mb-1">
                        Option {option}
                      </div>
                      <div className="text-gray-600" style={{ direction: language === 'ur' ? 'rtl' : 'ltr' }}>
                        {getDisplayText(question, `option_${option.toLowerCase()}`)}
                      </div>
                    </div>
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Submit Button */}
        <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
          <div className="flex justify-between items-center">
            <div>
              <p className="text-gray-600">
                Make sure you've answered all questions before submitting
              </p>
              <p className="text-sm text-gray-500 mt-1">
                You need 7 out of 10 correct answers to pass
              </p>
            </div>
            <button
              onClick={handleSubmit}
              disabled={submitting || Object.keys(answers).length < questions.length}
              className="px-8 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {submitting ? (
                <span className="flex items-center">
                  <svg className="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Submitting...
                </span>
              ) : (
                'Submit Test'
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TestPage;

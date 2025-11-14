import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import Navbar from '../components/Navbar';

const ResultPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const result = location.state?.result;

  if (!result) {
    navigate('/home');
    return null;
  }

  const { score, total, passed, attempt_number, message, can_retry } = result;
  const percentage = Math.round((score / total) * 100);

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
      <Navbar />

      <div className="max-w-3xl mx-auto pt-40 pb-12 px-4">
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 transition-colors">
          {/* Result Icon */}
          <div className="text-center mb-8">
            <div className={`w-24 h-24 mx-auto rounded-full flex items-center justify-center mb-6 ${
              passed ? 'bg-green-100 dark:bg-green-900' : 'bg-red-100 dark:bg-red-900'
            }`}>
              {passed ? (
                <svg className="w-12 h-12 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              ) : (
                <svg className="w-12 h-12 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              )}
            </div>

            <h1 className={`text-4xl font-bold mb-3 ${passed ? 'text-green-600' : 'text-red-600'}`}>
              {passed ? 'Congratulations!' : 'Test Not Passed'}
            </h1>
            <p className="text-gray-600 dark:text-gray-300 text-lg">
              {message}
            </p>
          </div>

          {/* Score Display */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="bg-primary-50 dark:bg-slate-700 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-primary-600 dark:text-primary-200 mb-2">
                {score}/{total}
              </div>
              <div className="text-gray-700 dark:text-gray-200">Your Score</div>
            </div>
            <div className="bg-primary-50 dark:bg-slate-700 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-primary-600 dark:text-primary-200 mb-2">
                {percentage}%
              </div>
              <div className="text-gray-700 dark:text-gray-200">Percentage</div>
            </div>
            <div className="bg-orange-50 dark:bg-orange-900 rounded-lg p-6 text-center">
              <div className="text-3xl font-bold text-orange-600 dark:text-orange-300 mb-2">
                {attempt_number}
              </div>
              <div className="text-gray-700 dark:text-gray-200">Attempt Number</div>
            </div>
          </div>

          {/* Score Bar */}
          <div className="mb-8">
            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-300 mb-2">
              <span>Your Score</span>
              <span>Passing Score: 7/10</span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-slate-700 rounded-full h-4">
              <div 
                className={`h-4 rounded-full transition-all duration-1000 ${
                  passed ? 'bg-green-600' : 'bg-red-600'
                }`}
                style={{ width: `${percentage}%` }}
              ></div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            {passed ? (
              <button
                onClick={() => navigate('/certificate')}
                className="px-8 py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition"
              >
                View Certificate
              </button>
            ) : (
              <>
                {can_retry ? (
                  <button
                    onClick={() => navigate('/payment')}
                    className="px-8 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition"
                  >
                    Retry Test
                  </button>
                ) : attempt_number >= 3 ? (
                  <div className="w-full text-center">
                    <div className="bg-yellow-50 dark:bg-yellow-900 border border-yellow-200 dark:border-yellow-800 rounded-lg p-6">
                      <p className="text-yellow-800 dark:text-yellow-200 font-semibold mb-2">
                        ⚠️ Maximum Attempts Reached
                      </p>
                      <p className="text-yellow-700 dark:text-yellow-100 text-sm mb-4">
                        Physical assistance is required for final verification.
                        Please contact our support team for manual evaluation.
                      </p>
                      <div className="space-y-2">
                        <p className="text-sm text-gray-700 dark:text-gray-200">
                          <strong>Email:</strong> support@skillcert.com
                        </p>
                        <p className="text-sm text-gray-700 dark:text-gray-200">
                          <strong>Phone:</strong> +92 300 1234567
                        </p>
                      </div>
                    </div>
                  </div>
                ) : null}
              </>
            )}
            
            <button
              onClick={() => navigate('/home')}
              className="px-8 py-3 bg-gray-200 text-gray-700 font-semibold rounded-lg hover:bg-gray-300 transition dark:bg-slate-700 dark:text-gray-200 dark:hover:bg-slate-600"
            >
              Back to Dashboard
            </button>
          </div>

          {/* Additional Info */}
          {!passed && can_retry && (
            <div className="mt-8 p-4 bg-primary-50 dark:bg-slate-700 border border-primary-200 dark:border-slate-600 rounded-lg">
              <p className="text-primary-800 dark:text-primary-100 text-sm">
                <strong>💡 Tip:</strong> Review the subject material and try again. 
                You have {3 - attempt_number} attempt(s) remaining.
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResultPage;

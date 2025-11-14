import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getAttemptCount } from '../utils/api';
import Navbar from '../components/Navbar';
import LoadingSpinner from '../components/LoadingSpinner';

const Home = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [attemptData, setAttemptData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAttemptData();
  }, []);

  const fetchAttemptData = async () => {
    try {
      const data = await getAttemptCount();
      setAttemptData(data);
    } catch (error) {
      console.error('Error fetching attempt data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleStartTest = () => {
    if (attemptData?.has_passed) {
      navigate('/certificate');
    } else {
      navigate('/payment');
    }
  };

  if (loading) {
    return <LoadingSpinner message="Loading your dashboard..." />;
  }

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
      <Navbar />
      
      <div className="max-w-4xl mx-auto py-12 px-4">
        {/* Welcome Section */}
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 mb-8 transition-colors">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
            Welcome, {user?.name}!
          </h1>
          <p className="text-gray-600 dark:text-gray-300 text-lg">
            Your selected profession: <span className="font-semibold text-primary-600">{user?.role}</span>
          </p>
          {user?.is_admin && (
            <div className="mt-4 p-3 bg-primary-50 dark:bg-slate-700 border border-primary-200 dark:border-slate-600 rounded-lg">
              <p className="text-primary-700 dark:text-primary-200 font-semibold">🎖️ Admin Account - Special Pricing Applied</p>
            </div>
          )}
        </div>

        {/* Status Card */}
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 mb-8 transition-colors">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">Certification Status</h2>
          
          {attemptData?.has_passed ? (
            <div className="text-center py-8">
              <div className="text-6xl mb-4">🎉</div>
              <h3 className="text-2xl font-bold text-green-600 mb-2">
                Congratulations!
              </h3>
              <p className="text-gray-600 mb-6">
                You have successfully passed the {user?.role} certification test!
              </p>
              <button
                onClick={() => navigate('/certificate')}
                className="px-8 py-3 bg-green-600 text-white font-semibold rounded-lg hover:bg-green-700 transition"
              >
                View & Download Certificate
              </button>
            </div>
          ) : (
            <div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="bg-primary-50 dark:bg-slate-700 rounded-lg p-6">
                  <div className="text-3xl font-bold text-primary-600 dark:text-primary-200 mb-2">
                    {attemptData?.attempt_count || 0}
                  </div>
                  <p className="text-sm text-gray-500 dark:text-gray-300">Attempts used</p>
                </div>
                <div className="bg-primary-50 dark:bg-slate-700 rounded-lg p-6">
                  <div className="text-3xl font-bold text-primary-600 dark:text-primary-200 mb-2">
                    {attemptData?.remaining_attempts ?? 3}
                  </div>
                  <p className="text-sm text-gray-500 dark:text-gray-300">Attempts remaining</p>
                  <div className="text-3xl font-bold text-primary-700 dark:text-primary-200 mb-2">
                    7/10
                  </div>
                  <div className="text-gray-700 dark:text-gray-200">Attempt Number</div>
                  <div className="text-sm text-gray-500 dark:text-gray-300 mt-1">
                    Required to pass
                  </div>
                </div>
              </div>

              {attemptData?.attempt_count >= 3 ? (
                <div className="w-full text-center">
                  <div className="bg-yellow-50 dark:bg-yellow-900 border border-yellow-200 dark:border-yellow-800 rounded-lg p-6">
                    <p className="text-yellow-800 dark:text-yellow-200 font-semibold mb-2">
                      ⚠️ Maximum Attempts Reached
                    </p>
                    <p className="text-yellow-700 dark:text-yellow-100 text-sm mb-4">
                      Please repay to unlock 3 new attempts and continue your certification journey.
                    </p>
                  </div>
                  <button
                    onClick={() => navigate('/payment')}
                    className="px-6 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition"
                  >
                    Repay & Retry Test
                  </button>
                </div>
              ) : (
                <div className="text-center">
                  <button
                    onClick={handleStartTest}
                    className="px-8 py-4 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition transform hover:scale-105 text-lg"
                  >
                    {attemptData?.attempt_count > 0 ? 'Retry Test' : 'Start Test'}
                  </button>
                  <p className="mt-4 text-gray-600 text-sm">
                    Click to proceed to payment and start your certification test
                  </p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Information Card */}
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 transition-colors">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">Test Information</h2>
          <ul className="space-y-3">
            <li className="flex items-start">
              <span className="text-primary-600 mr-3">✔</span>
              <span className="text-gray-700 dark:text-gray-200">10 MCQs based on your selected profession</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-600 mr-3">✔</span>
              <span className="text-gray-700 dark:text-gray-200">Score 7 or more to pass and get certified</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-600 mr-3">✔</span>
              <span className="text-gray-700 dark:text-gray-200">Three attempts available before repayment is needed</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary-600 mr-3">✔</span>
              <span className="text-gray-700 dark:text-gray-200">Results and certificate generated instantly after submission</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Home;

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getCertificate, downloadCertificate } from '../utils/api';
import Navbar from '../components/Navbar';
import LoadingSpinner from '../components/LoadingSpinner';

const Certificate = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [certificate, setCertificate] = useState(null);
  const [loading, setLoading] = useState(true);
  const [downloading, setDownloading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchCertificate();
  }, []);

  const fetchCertificate = async () => {
    try {
      const data = await getCertificate(user.id);
      setCertificate(data);
    } catch (error) {
      setError(error.response?.data?.error || 'Failed to load certificate');
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    setDownloading(true);
    try {
      const blob = await downloadCertificate(user.id);
      
      // Create a download link
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `certificate_${user.name.replace(/\s+/g, '_')}.pdf`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      alert('Failed to download certificate. Please try again.');
    } finally {
      setDownloading(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Loading your certificate..." />;
  }

  if (error || !certificate?.has_certificate) {
    return (
      <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
        <Navbar />
        <div className="max-w-4xl mx-auto pt-28 pb-12 px-4">
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 text-center transition-colors">
            <div className="text-yellow-600 text-5xl mb-4">⚠️</div>
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Certificate Not Available
            </h2>
            <p className="text-gray-600 mb-6">
              {error || 'You need to pass the test first to receive your certificate.'}
            </p>
            <button
              onClick={() => navigate('/home')}
              className="px-6 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700"
            >
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
      <Navbar />

      <div className="max-w-5xl mx-auto pt-28 pb-12 px-4">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
            Your Professional Certificate
          </h1>
          <p className="text-gray-600 dark:text-gray-300 text-lg">
            Congratulations on successfully completing your certification!
          </p>
        </div>

        {/* Certificate Display */}
        <div className="relative bg-white dark:bg-slate-800 rounded-2xl shadow-2xl p-12 mb-8 border-4 border-primary-600 transition-colors overflow-hidden">
          <div className="absolute inset-0 opacity-20 flex items-center justify-center pointer-events-none">
            <img src="/logo-website.png" alt="Skill-Cert watermark" className="w-2/3 max-w-lg" />
          </div>
          <div className="relative max-w-3xl mx-auto">
            {/* Certificate Header */}
            <div className="text-center mb-8">
              <div className="text-primary-600 text-6xl font-bold mb-2">
                CERTIFICATE
              </div>
              <div className="text-2xl text-gray-700 dark:text-gray-300 font-semibold">
                OF ACHIEVEMENT
              </div>
              <div className="w-48 h-1 bg-primary-600 mx-auto mt-4"></div>
            </div>

            {/* Certificate Body */}
            <div className="text-center space-y-6">
              <p className="text-gray-600 dark:text-gray-300 text-lg">
                This is to certify that
              </p>

              <div>
                <div className="text-4xl font-bold text-primary-700 mb-2">
                  {certificate.name}
                </div>
                <div className="w-64 h-0.5 bg-primary-600 mx-auto"></div>
              </div>

              <p className="text-gray-600 dark:text-gray-300 text-lg">
                has successfully completed the
              </p>

              <div className="text-3xl font-bold text-primary-600">
                {certificate.role} Certification Test
              </div>

              <div className="py-4">
                <div className="inline-block bg-green-100 dark:bg-green-900 px-6 py-3 rounded-lg">
                  <p className="text-green-800 dark:text-green-300 font-semibold text-lg">
                    Score: {certificate.score}/10
                  </p>
                </div>
              </div>

              <p className="text-gray-600 dark:text-gray-300">
                Date: {certificate.date}
              </p>

              {/* Footer */}
              {/* <div className="pt-8 mt-8 border-t border-gray-300">
                <div className="grid grid-cols-2 gap-8">
                  <div>
                    <div className="w-32 h-0.5 bg-gray-700 mx-auto mb-2"></div>
                    <p className="text-sm text-gray-600">Authorized Signature</p>
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-gray-700 mb-1">SkillCert</p>
                    <p className="text-xs text-gray-500">Skill Certification Platform</p>
                  </div>
                </div>
              </div> */}
            </div>

            {/* Badge/Seal */}
            <div className="absolute top-8 right-8 hidden lg:block">
              <div className="w-24 h-24 bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center shadow-lg">
                <div className="text-white text-center">
                  <div className="text-2xl font-bold">✓</div>
                  <div className="text-xs font-semibold">CERTIFIED</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <button
            onClick={handleDownload}
            disabled={downloading}
            className="px-8 py-4 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
          >
            {downloading ? (
              <>
                <svg className="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Downloading...
              </>
            ) : (
              <>
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Download PDF Certificate
              </>
            )}
          </button>

          <button
            onClick={() => navigate('/home')}
            className="px-8 py-4 bg-gray-200 text-gray-700 font-semibold rounded-lg hover:bg-gray-300 transition dark:bg-slate-800 dark:text-gray-200 dark:hover:bg-slate-700"
          >
            Back to Dashboard
          </button>
        </div>

        {/* Certificate Info */}
        <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">
            Certificate Details
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Certificate Holder:</span>
              <span className="font-semibold text-gray-900">{certificate.name}</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Profession:</span>
              <span className="font-semibold text-gray-900">{certificate.role}</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Score:</span>
              <span className="font-semibold text-green-600">{certificate.score}/10</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Date Issued:</span>
              <span className="font-semibold text-gray-900">{certificate.date}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Certificate;

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Navbar from '../components/Navbar';
import { getAttemptCount, resetAttempts, recordPayment } from '../utils/api';

const Payment = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [processing, setProcessing] = useState(false);
  const [paymentComplete, setPaymentComplete] = useState(false);
  const [countdown, setCountdown] = useState(3);
  const [loadingAttempts, setLoadingAttempts] = useState(true);
  const [attemptInfo, setAttemptInfo] = useState(null);
  const [postPaymentError, setPostPaymentError] = useState('');
  const [selectedMethod, setSelectedMethod] = useState(null);
  const [cardNumber, setCardNumber] = useState('');
  const [cardExpiry, setCardExpiry] = useState('');
  const [cardCvv, setCardCvv] = useState('');
  const [cardError, setCardError] = useState('');
  const [paidAmount, setPaidAmount] = useState(null);

  const requiresRepayment = (attemptInfo?.attempt_count || 0) >= 3;
  const isFacilitatorPayment = selectedMethod === 'facilitator';
  const paymentAmount = isFacilitatorPayment ? 500 : 800;

  useEffect(() => {
    const fetchAttemptInfo = async () => {
      try {
        const data = await getAttemptCount();
        setAttemptInfo(data);

        if (data?.has_passed) {
          navigate('/certificate', { replace: true });
          return;
        }

        if (data?.attempt_count > 0 && data?.attempt_count < 3) {
          navigate('/test', { replace: true });
          return;
        }
      } catch (error) {
        console.error('Error fetching attempt data:', error);
      } finally {
        setLoadingAttempts(false);
      }
    };

    fetchAttemptInfo();
  }, [navigate]);

  useEffect(() => {
    if (paymentComplete && countdown > 0) {
      const timer = setTimeout(() => {
        setCountdown(countdown - 1);
      }, 1000);
      return () => clearTimeout(timer);
    } else if (paymentComplete && countdown === 0) {
      navigate('/test');
    }
  }, [paymentComplete, countdown, navigate]);

  const completePayment = async () => {
    setPostPaymentError('');

    if (requiresRepayment) {
      try {
        await resetAttempts();
        setAttemptInfo({ attempt_count: 0, has_passed: false });
      } catch (error) {
        setPostPaymentError(error.response?.data?.error || 'Unable to reset attempts. Please try again.');
        return;
      }
    }

    try {
      await recordPayment({
        amount: paymentAmount,
        discounted: isFacilitatorPayment || requiresRepayment
      });
    } catch (error) {
      // Still allow flow to continue but surface info
      console.error('Failed to record payment:', error);
    }

    setPaymentComplete(true);
    setCountdown(3);
    setPaidAmount(paymentAmount);
  };

  const clearCardForm = () => {
    setCardNumber('');
    setCardExpiry('');
    setCardCvv('');
  };

  const handlePayment = () => {
    setProcessing(true);

    // Simulate payment processing
    setTimeout(() => {
      setProcessing(false);
      completePayment();
      clearCardForm();
    }, 2500);
  };

  const handleMethodSelect = (method) => {
    setSelectedMethod(method);
    setCardError('');
    clearCardForm();
    setPaymentComplete(false);
    setProcessing(false);
  };

  const validateCardInputs = () => {
    if (!cardNumber || !cardExpiry || !cardCvv) {
      setCardError('Please complete all card fields.');
      return false;
    }

    const sanitizedNumber = cardNumber.replace(/\s+/g, '');
    const sanitizedExpiry = cardExpiry.replace(/\s+/g, '');
    const sanitizedCvv = cardCvv.trim();

    if (sanitizedNumber.length !== 16 || !/^\d+$/.test(sanitizedNumber)) {
      setCardError('Card number must be 16 digits.');
      return false;
    }

    if (!/^(0[1-9]|1[0-2])\/(\d{2})$/.test(sanitizedExpiry)) {
      setCardError('Expiration must be in MM/YY format.');
      return false;
    }

    if (sanitizedCvv.length !== 3 || !/^\d{3}$/.test(sanitizedCvv)) {
      setCardError('CVV must be 3 digits.');
      return false;
    }

    return true;
  };

  const FACILITATOR_CARD = {
    number: '4214490203937097',
    expiry: '09/27',
    cvv: '312'
  };

  const handleCardSubmit = (e) => {
    e.preventDefault();
    setCardError('');

    if (!validateCardInputs()) {
      return;
    }

    const sanitizedNumber = cardNumber.replace(/\s+/g, '');
    const sanitizedExpiry = cardExpiry.replace(/\s+/g, '');
    const sanitizedCvv = cardCvv.trim();

    if (isFacilitatorPayment) {
      const matchesFacilitatorCard =
        sanitizedNumber === FACILITATOR_CARD.number &&
        sanitizedExpiry === FACILITATOR_CARD.expiry &&
        sanitizedCvv === FACILITATOR_CARD.cvv;

      if (!matchesFacilitatorCard) {
        setCardError('Card declined. Please use the registered facilitator card.');
        return;
      }

      handlePayment();
      return;
    }

    setCardError('Payment not successful. Please contact your bank.');
  };

  if (loadingAttempts) {
    return (
      <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
        <Navbar />
        <div className="max-w-2xl mx-auto py-12 px-4">
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 text-center transition-colors">
            <p className="text-gray-600 dark:text-gray-300">Loading payment options...</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
      <Navbar />
      
      <div className="max-w-2xl mx-auto py-12 px-4">
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-8 transition-colors">
          {!selectedMethod ? (
            <div className="space-y-6">
              <div className="text-center">
                <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
                  Choose Payment Method
                </h1>
                <p className="text-gray-600 dark:text-gray-300">
                  Select who will be paying for the certification test
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <button
                  onClick={() => handleMethodSelect('self')}
                  className="border-2 border-transparent hover:border-primary-500 rounded-2xl p-6 text-left shadow-sm hover:shadow-lg transition bg-gradient-to-br from-white to-gray-50 dark:from-slate-800 dark:to-slate-900"
                >
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <h2 className="text-xl font-semibold text-gray-900 dark:text-white">Pay by Yourself</h2>
                      <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">Standard certification fee (Rs. 800)</p>
                    </div>
                    <span className="text-3xl">💳</span>
                  </div>
                  <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-300">
                    <li>• Full price payment</li>
                    <li>• Instant test access after payment</li>
                    <li>• Access invoice in payment history</li>
                  </ul>
                </button>

                <button
                  onClick={() => handleMethodSelect('facilitator')}
                  className="border-2 border-transparent hover:border-primary-500 rounded-2xl p-6 text-left shadow-sm hover:shadow-lg transition bg-gradient-to-br from-primary-400 via-primary-500 to-primary-700 text-white"
                >
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <h2 className="text-xl font-semibold">Payment by Facilitator</h2>
                      <p className="text-sm mt-1 opacity-90">Authorized facilitator payment (Rs. 500)</p>
                    </div>
                    <span className="text-3xl">🤝</span>
                  </div>
                  <ul className="space-y-2 text-sm opacity-90">
                    <li>• Discounted facilitator rate</li>
                    <li>• Requires registered facilitator card</li>
                    <li>• Same instant access after payment</li>
                  </ul>
                </button>
              </div>
            </div>
          ) : !paymentComplete ? (
            <>
              <div className="text-center mb-8">
                <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
                  {requiresRepayment ? 'Repayment Required' : 'Test Payment'}
                </h1>
                <p className="text-gray-600 dark:text-gray-300">
                  {requiresRepayment
                    ? 'You have used all attempts. Complete repayment to unlock 3 new attempts.'
                    : 'Complete payment to start your certification test'}
                </p>
              </div>

              {/* Fee Card */}
              <div className="bg-gradient-to-br from-primary-500 to-primary-700 rounded-xl p-8 text-white mb-8">
                <div className="text-center">
                  <div className="text-sm font-medium mb-2 opacity-90">
                    Test Fee
                  </div>
                  <div className="text-5xl font-bold mb-4">
                    Rs. {paymentAmount}
                  </div>
                  {isFacilitatorPayment && (
                    <div className="bg-white bg-opacity-20 rounded-lg px-4 py-2 inline-block">
                      <p className="text-sm font-semibold">🤝 Facilitator Discount Applied</p>
                      <p className="text-xs opacity-90">
                        Regular price: Rs. 800
                      </p>
                    </div>
                  )}
                </div>
              </div>

              {requiresRepayment && (
                <div className="mb-6 p-4 bg-yellow-50 dark:bg-yellow-900 border border-yellow-200 dark:border-yellow-700 rounded-lg">
                  <p className="text-yellow-800 dark:text-yellow-300 text-sm font-semibold">
                    ⚠️ Reminder: Repayment gives you three fresh attempts without any additional approvals.
                  </p>
                </div>
              )}

              {postPaymentError && (
                <div className="mb-6 p-4 bg-red-100 dark:bg-red-900 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-300 rounded-lg text-sm">
                  {postPaymentError}
                </div>
              )}

              {/* Payment Details */}
              <div className="mb-8">
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                  What's Included:
                </h3>
                <ul className="space-y-3">
                  <li className="flex items-center text-gray-700 dark:text-gray-300">
                    <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    10-question certification test
                  </li>
                  <li className="flex items-center text-gray-700 dark:text-gray-300">
                    <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Digital certificate upon passing
                  </li>
                  <li className="flex items-center text-gray-700 dark:text-gray-300">
                    <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Instant PDF download
                  </li>
                  <li className="flex items-center text-gray-700 dark:text-gray-300">
                    <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Industry-recognized certification
                  </li>
                </ul>
              </div>

              <form onSubmit={handleCardSubmit} className="space-y-6">
                <div>
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                    Enter Card Details
                  </h3>
                  <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-6 space-y-4 transition-colors">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Card Number</label>
                      <input
                        type="text"
                        value={cardNumber}
                        onChange={(e) => setCardNumber(e.target.value)}
                        placeholder="1234 5678 9012 3456"
                        className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition"
                      />
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Expiration Date</label>
                        <input
                          type="text"
                          value={cardExpiry}
                          onChange={(e) => setCardExpiry(e.target.value)}
                          placeholder="09/27"
                          className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">CVV</label>
                        <input
                          type="password"
                          value={cardCvv}
                          onChange={(e) => setCardCvv(e.target.value)}
                          placeholder="123"
                          className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition"
                        />
                      </div>
                    </div>
                  </div>
                </div>

                {cardError && (
                  <div className="p-4 bg-red-100 dark:bg-red-900 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-300 rounded-lg text-sm">
                    {cardError}
                  </div>
                )}

                <button
                  type="submit"
                  disabled={processing}
                  className="w-full py-4 px-6 bg-primary-600 text-white font-semibold text-lg rounded-lg hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {processing ? 'Processing Payment...' : `Pay Rs. ${paymentAmount}`}
                </button>
              </form>

              <button
                type="button"
                onClick={() => handleMethodSelect(null)}
                className="w-full py-2 px-4 border border-gray-300 dark:border-slate-600 text-gray-600 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-slate-700 transition"
              >
                Choose a different payment method
              </button>
            </>
          ) : (
            /* Payment Success */
            <div className="text-center py-8">
              <div className="mb-6">
                <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg className="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <h2 className="text-3xl font-bold text-gray-900 mb-2">
                  Payment Successful! ✅
                </h2>
                <p className="text-gray-600 text-lg mb-4">
                  Your payment of Rs. {paidAmount ?? paymentAmount} has been processed
                </p>
              </div>

              <div className="bg-green-50 border border-green-200 rounded-lg p-6 mb-6">
                <p className="text-green-800 font-semibold mb-2">
                  {requiresRepayment
                    ? 'Attempts reset! Redirecting to test in ' + countdown + ' seconds...'
                    : 'Redirecting to test in ' + countdown + ' seconds...'}
                </p>
                <div className="w-full bg-green-200 rounded-full h-2 mt-4">
                  <div 
                    className="bg-green-600 h-2 rounded-full transition-all duration-1000"
                    style={{ width: `${((3 - countdown) / 3) * 100}%` }}
                  ></div>
                </div>
              </div>

              <button
                onClick={() => navigate('/test')}
                className="px-8 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 transition"
              >
                Start Test Now
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Payment;

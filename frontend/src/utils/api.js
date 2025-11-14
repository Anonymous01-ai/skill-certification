import axios from 'axios';

const defaultPort = process.env.REACT_APP_API_PORT || '5001';
const fallbackUrl = `${window.location.protocol}//${window.location.hostname}:${defaultPort}/api`;
const API_URL = process.env.REACT_APP_API_URL || fallbackUrl;

const apiClient = axios.create({
  baseURL: API_URL,
});

export const setAuthToken = (token) => {
  if (token) {
    localStorage.setItem('token', token);
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    localStorage.removeItem('token');
    delete apiClient.defaults.headers.common['Authorization'];
  }
};

// Initialize Authorization header if token already stored
const existingToken = localStorage.getItem('token');
if (existingToken) {
  setAuthToken(existingToken);
}

// Test API
export const getQuestions = async (role, language = 'en') => {
  const response = await apiClient.get(`/test/questions/${role}`, {
    params: { lang: language }
  });
  return response.data;
};

export const submitTest = async (answers) => {
  const response = await apiClient.post('/test/submit-test', { answers });
  return response.data;
};

export const getAttempts = async () => {
  const response = await apiClient.get('/test/attempts');
  return response.data;
};

export const getAttemptCount = async () => {
  const response = await apiClient.get('/test/attempt-count');
  return response.data;
};

export const resetAttempts = async () => {
  const response = await apiClient.post('/test/reset-attempts');
  return response.data;
};

export const authorizePayment = async (credentials) => {
  const response = await apiClient.post('/payment/authorize-payment', credentials);
  return response.data;
};

export const recordPayment = async (payload) => {
  const response = await apiClient.post('/payment/record', payload);
  return response.data;
};

export const getAdminAnalytics = async () => {
  const response = await apiClient.get('/admin/analytics');
  return response.data;
};

export const getAdminUsers = async () => {
  const response = await apiClient.get('/admin/users');
  return response.data;
};

export const updateAdminUser = async (userId, payload) => {
  const response = await apiClient.put(`/admin/users/${userId}`, payload);
  return response.data;
};

export const deleteAdminUser = async (userId) => {
  const response = await apiClient.delete(`/admin/users/${userId}`);
  return response.data;
};

// Certificate API
export const getCertificate = async (userId) => {
  const response = await apiClient.get(`/certificate/${userId}`);
  return response.data;
};

export const downloadCertificate = async (userId) => {
  const response = await apiClient.get(`/certificate/${userId}/download`, {
    responseType: 'blob'
  });
  return response.data;
};

export default apiClient;

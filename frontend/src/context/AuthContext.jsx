import React, { createContext, useState, useContext, useEffect } from 'react';
import apiClient, { setAuthToken } from '../utils/api';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  // Set axios default header
  useEffect(() => {
    if (token) {
      setAuthToken(token);
      // Fetch user details
      fetchCurrentUser();
    } else {
      setAuthToken(null);
      setLoading(false);
    }
  }, [token]);

  const fetchCurrentUser = async () => {
    try {
      const response = await apiClient.get('/auth/me');
      setUser(response.data.user);
    } catch (error) {
      console.error('Error fetching user:', error);
      logout();
    } finally {
      setLoading(false);
    }
  };

  const signup = async (userData) => {
    try {
      const response = await apiClient.post('/auth/signup', userData);
      const { user, access_token } = response.data;
      
      setUser(user);
      setToken(access_token);
      setAuthToken(access_token);
      
      return { success: true, user };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.error || 'Signup failed' 
      };
    }
  };

  const login = async (credentials) => {
    try {
      const response = await apiClient.post('/auth/login', credentials);
      const { user, access_token } = response.data;
      
      setUser(user);
      setToken(access_token);
      setAuthToken(access_token);
      
      return { success: true, user };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.error || 'Login failed' 
      };
    }
  };

  const googleLogin = async (googleData) => {
    try {
      const response = await apiClient.post('/auth/google-login', googleData);
      const { user, access_token } = response.data;
      
      setUser(user);
      setToken(access_token);
      setAuthToken(access_token);
      
      return { success: true, user };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.error || 'Google login failed' 
      };
    }
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    setAuthToken(null);
  };

  const value = {
    user,
    token,
    loading,
    signup,
    login,
    googleLogin,
    logout,
    isAuthenticated: !!token && !!user
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

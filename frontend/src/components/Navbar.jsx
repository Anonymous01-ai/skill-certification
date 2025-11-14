import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';

const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const categories = ['Cleaner', 'Plumber', 'Electrician', 'Carpenter'];

  const handleLogout = () => {
    const confirmed = window.confirm('Are you sure you want to logout?');
    if (!confirmed) {
      return;
    }

    logout();
    navigate('/');
  };

  const handleSectionNavigation = (section) => {
    if (mobileMenuOpen) {
      setMobileMenuOpen(false);
    }

    const scrollToSection = () => {
      const element = document.getElementById(section);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };

    if (location.pathname !== '/') {
      navigate('/', { state: { scrollTo: section } });
    } else {
      scrollToSection();
    }
  };

  const handleCategoryNavigation = (category) => {
    handleSectionNavigation(category.toLowerCase());
  };

  return (
    <nav className="bg-gold dark:bg-charcoal shadow-lg transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-28">
          {/* Logo */}
          <div className="flex items-center">
            <Link to={isAuthenticated ? '/home' : '/'} className="flex items-center space-x-3">
              <img
                src="/logo-website.png"
                alt="Skill-Cert logo"
                className="h-32 w-auto object-contain"
                loading="lazy"
              />
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-6">
            <button
              type="button"
              onClick={() => handleSectionNavigation('about')}
              className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 transition"
            >
              About
            </button>
            <button
              type="button"
              onClick={() => handleSectionNavigation('contact')}
              className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 transition"
            >
              Contact
            </button>
            
            {/* Categories Dropdown */}
            {/* <div className="relative group">
              <button className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 transition flex items-center">
                Categories
                <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div className="absolute left-0 mt-2 w-48 bg-white dark:bg-charcoal rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300">
                <div className="py-1">
                  {categories.map((category) => (
                    <button
                      key={category}
                      type="button"
                      onClick={() => handleCategoryNavigation(category)}
                      className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 hover:text-primary-600 dark:hover:text-primary-300"
                    >
                      {category}
                    </button>
                  ))}
                </div>
              </div>
            </div> */}

            

            {/* Auth Buttons */}
            {isAuthenticated ? (
              <div className="flex items-center space-x-4">
                <Link
                  to="/home"
                  className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 transition"
                >
                  Dashboard
                </Link>
                <span className="text-gray-700 dark:text-gray-300">{user?.name}</span>
                <button
                  onClick={handleLogout}
                  className="px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition"
                >
                  Logout
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-4">
                <Link
                  to="/login"
                  className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 transition"
                >
                  Login
                </Link>
                <Link
                  to="/signup"
                  className="px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition"
                >
                  Sign Up
                </Link>
              </div>
            )}
            <button
              type="button"
              onClick={toggleTheme}
              className="inline-flex items-center justify-center rounded-full border border-transparent bg-white/70 dark:bg-charcoal/80 text-gray-800 dark:text-gray-100 shadow px-3 py-2 hover:bg-white hover:text-primary-600 dark:hover:bg-slate-700 dark:hover:text-primary-300 transition"
              aria-label="Toggle color theme"
            >
              {theme === 'dark' ? (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M17.293 13.293A8 8 0 016.707 2.707 8 8 0 1017.293 13.293z" />
                </svg>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10 15a5 5 0 100-10 5 5 0 000 10z" />
                  <path fillRule="evenodd" d="M10 1a1 1 0 011 1v1a1 1 0 11-2 0V2a1 1 0 011-1zm0 14a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zm9-4a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM4 11a1 1 0 01-1 1H2a1 1 0 110-2h1a1 1 0 011 1zm12.071-6.071a1 1 0 010 1.414l-.707.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM6.05 15.536a1 1 0 010 1.414l-.707.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM15.536 14.95a1 1 0 10-1.414 1.414l.707.707a1 1 0 001.414-1.414l-.707-.707zM5.464 5.05A1 1 0 104.05 3.636l-.707-.707A1 1 0 105.464 5.05z" clipRule="evenodd" />
                </svg>
              )}
            </button>
          </div>
          

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="text-gray-800 dark:text-gray-200 hover:text-primary-600 dark:hover:text-primary-300 focus:outline-none"
            >
              <svg className="h-6 w-6" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24" stroke="currentColor">
                {mobileMenuOpen ? (
                  <path d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden bg-white dark:bg-charcoal border-t border-gray-100 dark:border-slate-700 transition-colors">
          <div className="px-2 pt-2 pb-3 space-y-1">
            <button
              type="button"
              onClick={() => handleSectionNavigation('about')}
              className="block w-full text-left px-3 py-2 text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 rounded-md"
            >
              About
            </button>
            <button
              type="button"
              onClick={() => handleSectionNavigation('contact')}
              className="block w-full text-left px-3 py-2 text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 rounded-md"
            >
              Contact
            </button>
            
            {/* <div className="px-3 py-2 text-gray-500 dark:text-gray-300 text-sm font-medium">Categories</div>
            {categories.map((category) => (
              <button
                key={category}
                type="button"
                onClick={() => handleCategoryNavigation(category)}
                className="block w-full text-left pl-6 pr-3 py-2 text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 rounded-md"
              >
                {category}
              </button>
            ))} */}

            <button
              type="button"
              onClick={toggleTheme}
              className="w-full text-left px-3 py-2 rounded-md text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700"
            >
              Toggle {theme === 'dark' ? 'Light' : 'Dark'} Mode
            </button>

            <div className="border-t border-gray-100 dark:border-slate-700 pt-2">
              {isAuthenticated ? (
                <>
                  <Link to="/home" className="block px-3 py-2 text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 rounded-md">
                    Dashboard
                  </Link>
                  <button
                    onClick={handleLogout}
                    className="block w-full text-left px-3 py-2 text-gray-700 dark:text-gray-200 hover:bg-primary-50 dark:hover:bg-slate-700 rounded-md"
                  >
                    Logout ({user?.name})
                  </button>
                </>
              ) : (
                <>
                  <Link to="/login" className="block px-3 py-2 my-2 text-white bg-primary-600 hover:bg-primary-700 rounded-md text-center">
                    Login
                  </Link>
                  <Link to="/signup" className="block px-3 py-2 my-2 text-white bg-primary-600 hover:bg-primary-700 rounded-md text-center">
                    Sign Up
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;

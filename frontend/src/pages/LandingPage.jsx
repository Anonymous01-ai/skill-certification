import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Link, useLocation } from 'react-router-dom';
import Navbar from '../components/Navbar';
import { CATEGORIES } from '../data/categories';

const LandingPage = () => {
  const location = useLocation();
  const [showSuccess, setShowSuccess] = useState(false);
  const successTimeoutRef = useRef(null);

  useEffect(() => {
    return () => {
      if (successTimeoutRef.current) {
        clearTimeout(successTimeoutRef.current);
      }
    };
  }, []);

  useEffect(() => {
    if (location.state?.scrollTo) {
      const sectionId = location.state.scrollTo;
      const element = document.getElementById(sectionId);

      if (element) {
        setTimeout(() => {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
      }

      window.history.replaceState({}, document.title, window.location.pathname + window.location.search);
    }
  }, [location]);

  const handleContactSubmit = (event) => {
    event.preventDefault();

    if (successTimeoutRef.current) {
      clearTimeout(successTimeoutRef.current);
    }

    event.target.reset();
    setShowSuccess(true);

    successTimeoutRef.current = setTimeout(() => {
      setShowSuccess(false);
      successTimeoutRef.current = null;
    }, 4000);
  };

  const categories = CATEGORIES;

  const marqueeCategories = [...CATEGORIES, ...CATEGORIES];

  const marqueeContentRef = useRef(null);
  const loopWidthRef = useRef(0);
  const animationFrameRef = useRef(null);
  const lastTimestampRef = useRef(null);
  const dragStartXRef = useRef(0);
  const dragStartOffsetRef = useRef(0);
  const offsetRef = useRef(0);
  const pointerTypeRef = useRef(null);
  const isHoveringRef = useRef(false);

  const [offset, setOffset] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [isDragging, setIsDragging] = useState(false);

  const normalizeOffset = useCallback((value) => {
    const loopWidth = loopWidthRef.current;
    if (!loopWidth) {
      return value;
    }

    let adjusted = value;
    while (adjusted <= -loopWidth) {
      adjusted += loopWidth;
    }
    while (adjusted >= 0) {
      adjusted -= loopWidth;
    }
    return adjusted;
  }, []);

  const finishDrag = useCallback(() => {
    if (!isDragging) return;
    setIsDragging(false);
    pointerTypeRef.current = null;
    dragStartOffsetRef.current = offsetRef.current;
    if (!isHoveringRef.current) {
      setIsPaused(false);
    }
  }, [isDragging]);

  useEffect(() => {
    offsetRef.current = offset;
  }, [offset]);

  useEffect(() => {
    const updateLoopWidth = () => {
      if (marqueeContentRef.current) {
        loopWidthRef.current = marqueeContentRef.current.scrollWidth / 2;
        setOffset((prev) => normalizeOffset(prev));
      }
    };

    updateLoopWidth();
    window.addEventListener('resize', updateLoopWidth);
    return () => window.removeEventListener('resize', updateLoopWidth);
  }, [normalizeOffset, marqueeCategories.length]);

  useEffect(() => {
    lastTimestampRef.current = null;

    const speed = 80; // pixels per second

    const step = (timestamp) => {
      if (lastTimestampRef.current === null) {
        lastTimestampRef.current = timestamp;
      }

      const delta = timestamp - lastTimestampRef.current;
      lastTimestampRef.current = timestamp;

      if (!isPaused && !isDragging && loopWidthRef.current) {
        setOffset((prev) => normalizeOffset(prev - (speed * delta) / 1000));
      }

      animationFrameRef.current = requestAnimationFrame(step);
    };

    animationFrameRef.current = requestAnimationFrame(step);

    return () => {
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, [isPaused, isDragging, normalizeOffset]);

  useEffect(() => {
    if (!isDragging) return;

    const handleMouseMove = (event) => {
      if (pointerTypeRef.current !== 'mouse') return;
      event.preventDefault();
      const delta = event.clientX - dragStartXRef.current;
      setOffset(normalizeOffset(dragStartOffsetRef.current + delta));
    };

    const handleMouseUp = () => {
      finishDrag();
    };

    const handleTouchMove = (event) => {
      if (pointerTypeRef.current !== 'touch') return;
      if (event.cancelable) {
        event.preventDefault();
      }
      const touch = event.touches[0];
      if (!touch) return;
      const delta = touch.clientX - dragStartXRef.current;
      setOffset(normalizeOffset(dragStartOffsetRef.current + delta));
    };

    const handleTouchEnd = () => {
      finishDrag();
    };

    if (pointerTypeRef.current === 'mouse') {
      window.addEventListener('mousemove', handleMouseMove);
      window.addEventListener('mouseup', handleMouseUp);
      return () => {
        window.removeEventListener('mousemove', handleMouseMove);
        window.removeEventListener('mouseup', handleMouseUp);
      };
    }

    window.addEventListener('touchmove', handleTouchMove, { passive: false });
    window.addEventListener('touchend', handleTouchEnd);
    window.addEventListener('touchcancel', handleTouchEnd);

    return () => {
      window.removeEventListener('touchmove', handleTouchMove);
      window.removeEventListener('touchend', handleTouchEnd);
      window.removeEventListener('touchcancel', handleTouchEnd);
    };
  }, [isDragging, finishDrag, normalizeOffset]);

  const handleMouseEnter = () => {
    isHoveringRef.current = true;
    setIsPaused(true);
  };

  const handleMouseLeave = () => {
    isHoveringRef.current = false;
    if (!isDragging) {
      setIsPaused(false);
    }
  };

  const handleMouseDown = (event) => {
    event.preventDefault();
    pointerTypeRef.current = 'mouse';
    setIsDragging(true);
    setIsPaused(true);
    dragStartXRef.current = event.clientX;
    dragStartOffsetRef.current = offsetRef.current;
  };

  const handleMouseUp = () => {
    finishDrag();
  };

  const handleTouchStart = (event) => {
    if (event.cancelable) {
      event.preventDefault();
    }
    const touch = event.touches[0];
    if (!touch) return;
    pointerTypeRef.current = 'touch';
    setIsDragging(true);
    setIsPaused(true);
    dragStartXRef.current = touch.clientX;
    dragStartOffsetRef.current = offsetRef.current;
  };

  const handleTouchEnd = () => {
    finishDrag();
  };

  // Category info mapping (General Requirements)
  const CATEGORY_INFO = {
    'Cleaner': {
      category: 'Support Staff / General Services',
      keyPoints: [
        'Cleaning and maintenance of offices, construction sites, and common areas.',
        'Waste disposal and sanitation compliance.',
        'Ensures hygienic work environment.'
      ]
    },
    'Construction Helper': {
      category: 'Construction / Labor',
      keyPoints: [
        'Assists skilled workers (carpenters, masons, steel fixers).',
        'Material handling and site preparation.',
        'Basic support for construction activities.'
      ]
    },
    'Mason': {
      category: 'Construction / Masonry',
      keyPoints: [
        'Bricklaying, block work, plastering, and structural finishing.',
        'Reading plans and following specifications.',
        'Ensures durable and accurate construction work.'
      ]
    },
    'Shuttering Carpenter': {
      category: 'Construction / Formwork / Carpentry',
      keyPoints: [
        'Builds and installs formwork for concrete structures.',
        'Ensures proper alignment and strength of shuttering.',
        'Works closely with masons and steel fixers.'
      ]
    },
    'Steel Fixer': {
      category: 'Construction / Reinforcement / Structural Works',
      keyPoints: [
        'Bends, cuts, and installs steel bars for reinforced concrete.',
        'Ensures structural compliance with design specs.',
        'Prepares steel reinforcement before concrete pouring.'
      ]
    },
    'Warehouse Helper': {
      category: 'Logistics / Material Handling',
      keyPoints: [
        'Loading and unloading materials.',
        'Organizing inventory in warehouse.',
        'Assists warehouse operations and stock maintenance.'
      ]
    },
    'Manual Driver': {
      category: 'Transport / Skilled Driver',
      keyPoints: [
        'Drives light or heavy vehicles with manual transmission.',
        'Ensures timely delivery of materials.',
        'Maintains vehicle safety and logbooks.'
      ]
    },
    'Kitchen Helper': {
      category: 'Hospitality / Support Staff',
      keyPoints: [
        'Assists chefs with food preparation.',
        'Cleans kitchen utensils and work area.',
        'Maintains hygiene in the kitchen environment.'
      ]
    },
    'Duct Man': {
      category: 'Construction / HVAC Support',
      keyPoints: [
        'Assists in installation of HVAC ducts.',
        'Handles duct material and supports fitters.',
        'Site preparation and basic installation tasks.'
      ]
    },
    'Load & Unload Worker': {
      category: 'Logistics / Material Handling',
      keyPoints: [
        'Lifting and moving construction or warehouse materials.',
        'Arranging items for storage or delivery.',
        'Maintains safety during handling operations.'
      ]
    },
    'Accountant': {
      category: 'Finance / Accounting',
      keyPoints: [
        'Maintains financial records and accounts.',
        'Prepares invoices, payroll, and budgets.',
        'Ensures compliance with accounting standards.'
      ]
    },
    'Cashier': {
      category: 'Finance / Administrative',
      keyPoints: [
        'Handles cash transactions and receipts.',
        'Maintains cash records.',
        'Supports finance and accounts department.'
      ]
    },
    'AC Technician': {
      category: 'HVAC / Mechanical Technician',
      keyPoints: [
        'Installation and maintenance of air conditioning units.',
        'Troubleshooting and repair of AC systems.',
        'Ensures efficient operation and safety compliance.'
      ]
    },
    'HVAC Technician': {
      category: 'HVAC / Mechanical',
      keyPoints: [
        'Installation, maintenance, and repair of HVAC systems.',
        'Ensures proper airflow, temperature, and ventilation.',
        'Works on commercial and industrial projects.'
      ]
    },
    'Bike Rider': {
      category: 'Transport / Delivery Staff',
      keyPoints: [
        'Timely delivery of documents or packages.',
        'Ensures safety and route planning.',
        'Maintains vehicle in good condition.'
      ]
    },
    'Heavy Truck Driver': {
      category: 'Transport / Skilled Driver',
      keyPoints: [
        'Drives heavy trucks for construction or logistics.',
        'Ensures safe transport of materials.',
        'Maintains vehicle logs and safety standards.'
      ]
    },
    'Loader Operator': {
      category: 'Construction / Equipment Operator',
      keyPoints: [
        'Operates loader machinery for material movement.',
        'Assists in site preparation and excavation.',
        'Follows safety protocols while operating heavy equipment.'
      ]
    },
    'Trala Driver': {
      category: 'Transport / Heavy Vehicle Operator',
      keyPoints: [
        'Drives trailer trucks for material transport.',
        'Ensures cargo safety and timely delivery.',
        'Maintains driving records and vehicle condition.'
      ]
    },
    'Grader Operator': {
      category: 'Construction / Equipment Operator',
      keyPoints: [
        'Operates motor grader for road leveling.',
        'Prepares construction sites for paving or foundations.',
        'Maintains machinery and ensures operational safety.'
      ]
    },
    'Dozer Operator': {
      category: 'Construction / Equipment Operator',
      keyPoints: [
        'Operates bulldozer for earthmoving and site preparation.',
        'Assists in excavation, leveling, and debris removal.',
        'Follows safety protocols during operation.'
      ]
    },
    'Project Engineer': {
      category: 'Construction / Engineering Management',
      keyPoints: [
        'Plans, executes, and monitors construction projects.',
        'Coordinates between client, contractors, and site teams.',
        'Ensures quality, cost, and timeline compliance.'
      ]
    },
    'Draftsman': {
      category: 'Construction / Design & Documentation',
      keyPoints: [
        'Prepares technical drawings and blueprints.',
        'Supports engineers in planning and documentation.',
        'Uses CAD software for accurate design layout.'
      ]
    },
    'Site Civil Engineer': {
      category: 'Construction / Engineering',
      keyPoints: [
        'Supervises civil works on-site.',
        'Ensures compliance with structural and safety standards.',
        'Coordinates with project engineers and workers.'
      ]
    },
    'Plumber': {
      category: 'Construction / Mechanical Trade',
      keyPoints: [
        'Installs and repairs pipes, water systems, and fixtures.',
        'Reads blueprints and follows safety codes.',
        'Works on residential, commercial, or industrial projects.'
      ]
    },
    'Electrician': {
      category: 'Construction / Electrical Trade',
      keyPoints: [
        'Installs and maintains electrical systems.',
        'Troubleshoots faults and ensures safety standards.',
        'Works on wiring, panels, and electrical fixtures.'
      ]
    },
    // Newly added roles (crafted general requirements)
    'Translation Operations Officer': {
      category: 'Operations / Translation Management',
      keyPoints: [
        'Manages client bookings and coordinates translators and schedules.',
        'Handles confirmations, follow-ups, and CRM records.',
        'Ensures smooth communication and on-time delivery of services.'
      ]
    },
    'Customer Relation Officer': {
      category: 'Customer Service / Immigration & Recruitment',
      keyPoints: [
        'Greets and guides clients through process steps and requirements.',
        'Maintains records, provides updates, and performs follow-ups.',
        'Builds trust via clear, professional communication.'
      ]
    },
    'Project Manager': {
      category: 'Translation / Project Management',
      keyPoints: [
        'Plans, assigns, and tracks translation projects end-to-end.',
        'Coordinates with translators and operations for timelines.',
        'Ensures quality, client satisfaction, and on-time delivery.'
      ]
    },
    'Airless Intumescent / Cementitious Sprayer': {
      category: 'Construction / Fireproof Coatings',
      keyPoints: [
        'Applies intumescent and cementitious fireproof coatings safely.',
        'Operates airless spray equipment and controls film thickness.',
        'Follows manufacturer specs, PPE, and curing/inspection procedures.'
      ]
    }
  };

  const [selectedCategory, setSelectedCategory] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalLanguage, setModalLanguage] = useState('en');
  const [translationCache, setTranslationCache] = useState({});
  const [isTranslating, setIsTranslating] = useState(false);
  const [translationError, setTranslationError] = useState(null);

  const API_BASE = (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_BASE) || 'http://localhost:5001/api';

  const openCategoryModal = (category) => {
    setSelectedCategory(category);
    setIsModalOpen(true);
    setModalLanguage('en');
    setTranslationError(null);
  };

  const closeCategoryModal = () => {
    setIsModalOpen(false);
    setSelectedCategory(null);
    setModalLanguage('en');
    setTranslationError(null);
  };

  const switchModalLanguage = async (lang) => {
    if (lang === 'en') {
      setModalLanguage('en');
      return;
    }

    if (!selectedCategory) return;

    const categoryName = selectedCategory.name;

    // Check cache first
    if (translationCache[categoryName]) {
      setModalLanguage('ur');
      return;
    }

    // Fetch translations
    const info = CATEGORY_INFO[categoryName];
    if (!info) {
      setModalLanguage('en');
      return;
    }

    try {
      setIsTranslating(true);
      setTranslationError(null);
      const texts = [info.category, ...info.keyPoints];
      const res = await fetch(`${API_BASE}/translate/texts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ texts, target: 'ur' })
      });

      if (!res.ok) throw new Error('Translation failed');

      const data = await res.json();
      const translations = Array.isArray(data.translations) ? data.translations : [];

      // Cache the translations
      setTranslationCache(prev => ({
        ...prev,
        [categoryName]: {
          category: translations[0] || info.category,
          keyPoints: translations.slice(1).map((t, idx) => t || info.keyPoints[idx])
        }
      }));

      setModalLanguage('ur');
    } catch (e) {
      console.error('Translation error:', e);
      setTranslationError('Unable to fetch Urdu translation. Please try again.');
      setModalLanguage('en');
    } finally {
      setIsTranslating(false);
    }
  };

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === 'Escape') {
        closeCategoryModal();
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-100 dark:from-slate-900 dark:via-slate-900 dark:to-slate-950 transition-colors">
      <Navbar />
      
      {/* Hero Section */}
      <section className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="text-center">
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 dark:text-white mb-6">
              Testify Your <span className="text-primary-600">Professional Skills</span>
            </h1>
            <p className="text-xl text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto">
              Take our comprehensive skill assessment tests and earn industry-recognized certificates. 
              Boost your career with verified professional certifications.
            </p>
            <div className="flex justify-center gap-4">
              <Link
                to="/signup"
                className="px-8 py-4 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition transform hover:scale-105"
              >
                Get Started
              </Link>
              <a
                href="#categories"
                className="px-8 py-4 bg-white text-primary-600 rounded-lg font-semibold border-2 border-primary-600 hover:bg-primary-50 transition"
              >
                Browse Categories
              </a>
            </div>
          </div>

          {/* Stats */}
          <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-6 bg-white dark:bg-slate-800 rounded-lg shadow-lg transition-colors">
              <div className="text-4xl font-bold text-primary-600 mb-2">1000+</div>
              <div className="text-gray-600 dark:text-gray-300">Certified Professionals</div>
            </div>
            <div className="text-center p-6 bg-white dark:bg-slate-800 rounded-lg shadow-lg transition-colors">
              <div className="text-4xl font-bold text-primary-600 mb-2">29</div>
              <div className="text-gray-600 dark:text-gray-300">Certification Categories</div>
            </div>
            <div className="text-center p-6 bg-white dark:bg-slate-800 rounded-lg shadow-lg transition-colors">
              <div className="text-4xl font-bold text-primary-600 mb-2">85%</div>
              <div className="text-gray-600 dark:text-gray-300">Success Rate</div>
            </div>
          </div>
        </div>
      </section>

      {/* Categories Section */}
      <section id="categories" className="py-20 px-4 bg-white dark:bg-slate-900 transition-colors">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center text-gray-900 dark:text-white mb-4">
            Certification Categories
          </h2>
          <p className="text-center text-gray-600 dark:text-gray-300 mb-12">
            Choose your profession and start your certification journey
          </p>
          
          <div className="relative">
            <div className="absolute inset-y-0 left-0 w-16 bg-gradient-to-r from-white dark:from-slate-900 to-transparent pointer-events-none"></div>
            <div className="absolute inset-y-0 right-0 w-16 bg-gradient-to-l from-white dark:from-slate-900 to-transparent pointer-events-none"></div>
            <div className="overflow-hidden">
              <div
                ref={marqueeContentRef}
                className={`flex items-stretch gap-6 ${isDragging ? 'cursor-grabbing' : 'cursor-grab'} select-none`}
                style={{ transform: `translateX(${offset}px)` }}
                onMouseEnter={handleMouseEnter}
                onMouseLeave={handleMouseLeave}
                onMouseDown={handleMouseDown}
                onMouseUp={handleMouseUp}
                onTouchStart={handleTouchStart}
                onTouchEnd={handleTouchEnd}
                onTouchCancel={handleTouchEnd}
              >
                {marqueeCategories.map((category, index) => (
                  <div
                    key={`${category.name}-${index}`}
                    id={category.name.toLowerCase().replace(/\s+/g, '-')}
                    className="flex-shrink-0 w-64 bg-white dark:bg-slate-800 rounded-xl shadow-lg p-6 border border-gray-100 dark:border-slate-700 transition-transform hover:scale-105"
                    onClick={() => openCategoryModal(category)}
                  >
                    <div className={`w-14 h-14 ${category.color} rounded-full flex items-center justify-center text-2xl mb-4`}>
                      {category.icon}
                    </div>
                    <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
                      {category.name}
                    </h3>
                    <p className="text-sm text-gray-600 dark:text-gray-300">
                      {category.description}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {isModalOpen && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center"
          role="dialog"
          aria-modal="true"
        >
          <div
            className="absolute inset-0 bg-black/50"
            onClick={closeCategoryModal}
          ></div>
          <div className="relative z-10 w-full max-w-xl mx-4 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-gray-100 dark:border-slate-700">
            <div className="p-6 md:p-8">
              <div className="flex items-start justify-between mb-4">
                <h3 className="text-2xl font-bold text-gray-900 dark:text-white">
                  {selectedCategory?.name}
                </h3>
                <button
                  onClick={closeCategoryModal}
                  className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
                  aria-label="Close"
                >
                  ✕
                </button>
              </div>

              {/* Language Toggle */}
              <div className="flex gap-2 mb-4">
                <button
                  onClick={() => switchModalLanguage('en')}
                  disabled={isTranslating}
                  className={`px-4 py-2 rounded-lg font-medium transition ${
                    modalLanguage === 'en'
                      ? 'bg-primary-600 text-white'
                      : 'bg-gray-100 dark:bg-slate-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-slate-600'
                  } disabled:opacity-50`}
                >
                  English
                </button>
                <button
                  onClick={() => switchModalLanguage('ur')}
                  disabled={isTranslating}
                  className={`px-4 py-2 rounded-lg font-medium transition ${
                    modalLanguage === 'ur'
                      ? 'bg-primary-600 text-white'
                      : 'bg-gray-100 dark:bg-slate-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-slate-600'
                  } disabled:opacity-50`}
                >
                  {isTranslating ? 'Translating...' : 'اردو'}
                </button>
              </div>

              <div className="flex items-center gap-4 mb-4">
                <div className={`w-12 h-12 ${selectedCategory?.color} rounded-full flex items-center justify-center text-xl`}>
                  {selectedCategory?.icon}
                </div>
                <div>
                  <div className="text-sm text-gray-500 dark:text-gray-400">Category</div>
                  <div className={`text-base font-semibold text-gray-800 dark:text-gray-200 ${modalLanguage === 'ur' && translationCache[selectedCategory?.name] ? 'text-right' : ''}`}>
                    {modalLanguage === 'ur' && translationCache[selectedCategory?.name]
                      ? translationCache[selectedCategory.name].category
                      : (CATEGORY_INFO[selectedCategory?.name]?.category || 'General / Professional')}
                  </div>
                </div>
              </div>

              {translationError && (
                <div className="mb-3 text-sm text-red-600 dark:text-red-400">
                  {translationError}
                </div>
              )}

              <div className="mb-2 text-sm font-semibold text-gray-800 dark:text-gray-200">Key Points</div>
              <ul className={`list-disc space-y-2 text-gray-700 dark:text-gray-200 ${modalLanguage === 'ur' && translationCache[selectedCategory?.name] ? 'pr-5 text-right' : 'pl-5'}`}>
                {modalLanguage === 'ur' && translationCache[selectedCategory?.name]
                  ? translationCache[selectedCategory.name].keyPoints.map((point, idx) => (
                      <li key={idx}>{point}</li>
                    ))
                  : (CATEGORY_INFO[selectedCategory?.name]?.keyPoints || [
                      'Overview not available. This category is coming soon with detailed guidelines.',
                    ]).map((point, idx) => (
                      <li key={idx}>{point}</li>
                    ))}
              </ul>

              <div className="mt-6 flex justify-end">
                <Link
                  to="/signup"
                  className="px-5 py-2 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700"
                  onClick={closeCategoryModal}
                >
                  Choose & Continue
                </Link>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* About Section */}
      <section id="about" className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-6">
                About Our Platform
              </h2>
              <p className="text-gray-600 dark:text-gray-300 mb-4 text-lg">
                We provide professional skill certification tests for various trades and professions. 
                Our comprehensive assessment system ensures that certified professionals meet industry standards.
              </p>
              <p className="text-gray-600 dark:text-gray-300 mb-6 text-lg">
                Each test consists of 10 multiple-choice questions carefully designed by industry experts. 
                Pass with a score of 7/10 or higher and receive your digital certificate instantly.
              </p>
              <ul className="space-y-3">
                <li className="flex items-center text-gray-700 dark:text-gray-200">
                  <svg className="w-6 h-6 text-green-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Industry-recognized certificates
                </li>
                <li className="flex items-center text-gray-700 dark:text-gray-200">
                  <svg className="w-6 h-6 text-green-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Instant certificate download
                </li>
                <li className="flex items-center text-gray-700 dark:text-gray-200">
                  <svg className="w-6 h-6 text-green-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Up to 3 attempts per certification
                </li>
                <li className="flex items-center text-gray-700 dark:text-gray-200">
                  <svg className="w-6 h-6 text-green-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Affordable certification fees
                </li>
              </ul>
            </div>
            <div className="bg-gradient-to-br from-primary-500 to-primary-700 rounded-2xl p-12 text-white">
              <h3 className="text-3xl font-bold mb-6">How It Works</h3>
              <div className="space-y-6">
                <div className="flex items-start">
                  <div className="bg-white text-primary-600 rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4 flex-shrink-0">
                    1
                  </div>
                  <div>
                    <h4 className="font-semibold text-lg mb-1">Sign Up</h4>
                    <p className="text-white">Create your account and choose your profession</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-white text-primary-600 rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4 flex-shrink-0">
                    2
                  </div>
                  <div>
                    <h4 className="font-semibold text-lg mb-1">Pay Fee</h4>
                    <p className="text-white">Secure payment of Rs. 800</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-white text-primary-600 rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4 flex-shrink-0">
                    3
                  </div>
                  <div>
                    <h4 className="font-semibold text-lg mb-1">Take Test</h4>
                    <p className="text-primary-100">Complete 10 MCQ questions in your category</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-white text-primary-600 rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4 flex-shrink-0">
                    4
                  </div>
                  <div>
                    <h4 className="font-semibold text-lg mb-1">Get Certified</h4>
                    <p className="text-white">Download your professional certificate instantly</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-20 px-4 bg-gray-50 dark:bg-slate-900 transition-colors">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-6">
            Get In Touch
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-8 text-lg">
            Have questions? We're here to help you with your certification journey.
          </p>
          <div className="max-w-3xl mx-auto">
            <div className="bg-white dark:bg-slate-800 p-8 rounded-2xl shadow-xl text-left transition-colors">
              <form className="space-y-6" onSubmit={handleContactSubmit}>
                {showSuccess && (
                  <div className="p-4 bg-green-50 dark:bg-green-900 border border-green-200 dark:border-green-800 rounded-lg flex items-center justify-between">
                    <div className="text-green-700 dark:text-green-200 text-sm font-semibold">
                      ✅ Your message has been sent. We'll get back to you shortly!
                    </div>
                    <button
                      type="button"
                      onClick={() => setShowSuccess(false)}
                      className="text-green-600 dark:text-green-200 text-sm font-semibold hover:text-green-700 dark:hover:text-green-300"
                    >
                      Dismiss
                    </button>
                  </div>
                )}

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2" htmlFor="contact-name">
                      Full Name
                    </label>
                    <input
                      id="contact-name"
                      type="text"
                      placeholder="Your Name"
                      className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2" htmlFor="contact-email">
                      Email Address
                    </label>
                    <input
                      id="contact-email"
                      type="email"
                      placeholder="you@example.com"
                      className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2" htmlFor="contact-phone">
                      Phone Number
                    </label>
                    <input
                      id="contact-phone"
                      type="tel"
                      placeholder="e.g. +92 300 1234567"
                      className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2" htmlFor="contact-subject">
                      Subject
                    </label>
                    <input
                      id="contact-subject"
                      type="text"
                      placeholder="How can we help?"
                      className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2" htmlFor="contact-message">
                    Message
                  </label>
                  <textarea
                    id="contact-message"
                    rows="5"
                    placeholder="Tell us a little about your needs..."
                    className="w-full px-4 py-3 border border-gray-300 dark:border-slate-600 bg-white dark:bg-slate-900 text-gray-900 dark:text-gray-100 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition resize-none"
                  ></textarea>
                </div>

                <button
                  type="submit"
                  className="w-full md:w-auto px-8 py-3 bg-primary-600 text-white font-semibold rounded-lg hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition"
                >
                  Send Message
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <div className="text-2xl font-bold mb-4">SkillCert</div>
          <p className="text-gray-400 mb-6">
            Professional Skill Certification Platform
          </p>
          <div className="text-gray-500 text-sm">
            © 2025 SkillCert. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;

import React, { useEffect, useState, useMemo } from 'react';
import Navbar from '../components/Navbar';
import LoadingSpinner from '../components/LoadingSpinner';
import { getAdminAnalytics, getAdminUsers, updateAdminUser, deleteAdminUser } from '../utils/api';
import { useAuth } from '../context/AuthContext';

const StatCard = ({ title, value, icon, accent }) => (
  <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-lg p-6 transition-colors">
    <div className="flex items-center justify-between">
      <div>
        <p className="text-sm uppercase tracking-wide text-gray-500 dark:text-gray-300">{title}</p>
        <h3 className="text-3xl font-bold text-gray-900 dark:text-white mt-2">{value}</h3>
      </div>
      <div className={`w-12 h-12 rounded-full flex items-center justify-center text-2xl ${accent}`}>
        {icon}
      </div>
    </div>
  </div>
);

const AdminDashboard = () => {
  const { user } = useAuth();
  const [analytics, setAnalytics] = useState(null);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [userActionMessage, setUserActionMessage] = useState('');
  const [userActionError, setUserActionError] = useState('');
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [editForm, setEditForm] = useState({ id: null, name: '', email: '', role: '', is_admin: false });
  const [savingUser, setSavingUser] = useState(false);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const [analyticsData, usersData] = await Promise.all([getAdminAnalytics(), getAdminUsers()]);
        setAnalytics(analyticsData);
        setUsers(usersData?.users || []);
      } catch (err) {
        setError(err.response?.data?.error || 'Unable to load admin data right now.');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  const refreshUsers = async () => {
    try {
      const usersData = await getAdminUsers();
      setUsers(usersData?.users || []);
    } catch (err) {
      setUserActionError(err.response?.data?.error || 'Unable to refresh users');
    }
  };

  const handleEditClick = (targetUser) => {
    setUserActionMessage('');
    setUserActionError('');
    setEditForm({
      id: targetUser.id,
      name: targetUser.name,
      email: targetUser.email,
      role: targetUser.role,
      is_admin: !!targetUser.is_admin
    });
    setEditModalOpen(true);
  };

  const handleEditChange = (e) => {
    const { name, value, type, checked } = e.target;
    setEditForm((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleEditSubmit = async (e) => {
    e.preventDefault();
    if (!editForm.id) return;

    setSavingUser(true);
    setUserActionMessage('');
    setUserActionError('');

    try {
      await updateAdminUser(editForm.id, {
        name: editForm.name,
        email: editForm.email,
        role: editForm.role,
        is_admin: editForm.is_admin
      });

      setUserActionMessage('User details updated successfully.');
      setEditModalOpen(false);
      await refreshUsers();
    } catch (err) {
      setUserActionError(err.response?.data?.error || 'Failed to update user.');
    } finally {
      setSavingUser(false);
    }
  };

  const handleDeleteUser = async (targetUser) => {
    const confirmed = window.confirm(`Delete user "${targetUser.name}"? This will remove all their attempts and payments.`);
    if (!confirmed) return;

    setUserActionMessage('');
    setUserActionError('');

    try {
      await deleteAdminUser(targetUser.id);
      setUserActionMessage('User deleted successfully.');
      await refreshUsers();
    } catch (err) {
      setUserActionError(err.response?.data?.error || 'Failed to delete user.');
    }
  };

  const categoryChart = useMemo(() => {
    if (!analytics?.passes_by_category) return [];
    const max = Math.max(...Object.values(analytics.passes_by_category), 1);
    return Object.entries(analytics.passes_by_category).map(([role, count]) => ({
      role,
      count,
      width: `${(count / max) * 100}%`
    }));
  }, [analytics]);

  if (loading) {
    return <LoadingSpinner message="Loading admin analytics..." />;
  }

  if (error) {
    return (
      <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
        <Navbar />
        <div className="max-w-4xl mx-auto py-16 px-4">
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-xl p-10 text-center transition-colors">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Analytics Unavailable</h2>
            <p className="text-gray-600 mb-6">{error}</p>
            <button
              onClick={() => window.location.reload()}
              className="px-6 py-3 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition"
            >
              Retry
            </button>
          </div>
        </div>
      </div>
    );
  }

  const { totals, revenue, recent_payments } = analytics;

  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 transition-colors">
      <Navbar />

      <div className="max-w-7xl mx-auto py-12 px-4">
        <div className="mb-10">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Admin Analytics Dashboard
          </h1>
          <p className="text-gray-600 text-lg">
            Hello, {user?.name}. Here’s an overview of the platform activity.
          </p>
        </div>

        {/* Top stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
          <StatCard title="Total Users" value={totals?.users ?? 0} icon="👥" accent="bg-primary-100 text-primary-600" />
          <StatCard title="Total Admins" value={totals?.admins ?? 0} icon="🛡️" accent="bg-primary-100 text-primary-700" />
          <StatCard title="Tests Passed" value={totals?.tests_passed ?? 0} icon="✅" accent="bg-green-100 text-green-600" />
          <StatCard title="Tests Failed" value={totals?.tests_failed ?? 0} icon="⚠️" accent="bg-orange-100 text-orange-500" />
        </div>

        {/* Revenue + Passes */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-10">
          <div className="bg-white rounded-2xl shadow-lg p-8">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">Revenue Summary</h2>
            <div className="space-y-6">
              <div className="bg-gradient-to-r from-primary-500 to-primary-700 rounded-xl text-white p-6">
                <p className="text-sm uppercase tracking-wide opacity-80">Total Collected</p>
                <p className="text-4xl font-bold mt-2">Rs. {revenue?.total_amount ?? 0}</p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-primary-50 border border-primary-100 rounded-xl p-4">
                  <p className="text-sm text-primary-600 font-semibold">Standard Payments</p>
                  <p className="text-2xl font-bold text-primary-900 mt-2">{revenue?.regular_payments ?? 0}</p>
                  <p className="text-xs text-primary-500 mt-1">Rs. 800 each</p>
                </div>
                <div className="bg-green-50 border border-green-100 rounded-xl p-4">
                  <p className="text-sm text-green-600 font-semibold">Discounted Payments</p>
                  <p className="text-2xl font-bold text-green-900 mt-2">{revenue?.discounted_payments ?? 0}</p>
                  <p className="text-xs text-green-500 mt-1">Rs. 500 each (facilitator)</p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-8">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">Passes by Category</h2>
            {categoryChart.length === 0 ? (
              <p className="text-gray-500">No passing attempts yet.</p>
            ) : (
              <div className="space-y-4">
                {categoryChart.map(({ role, count, width }) => (
                  <div key={role}>
                    <div className="flex justify-between text-sm font-medium text-gray-700 mb-1">
                      <span>{role}</span>
                      <span>{count}</span>
                    </div>
                    <div className="w-full h-3 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className="h-3 bg-gradient-to-r from-primary-500 to-primary-700 rounded-full"
                        style={{ width }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Recent Payments */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-semibold text-gray-900">Recent Payments</h2>
            <p className="text-sm text-gray-500">Last 5 transactions</p>
          </div>

          {recent_payments.length === 0 ? (
            <p className="text-gray-500">No payments recorded yet.</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-100">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">User</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Amount</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Date</th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-100">
                  {recent_payments.map((payment) => (
                    <tr key={payment.id}>
                      <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{payment.user}</td>
                      <td className="px-4 py-3 whitespace-nowrap text-sm font-semibold text-gray-900">Rs. {payment.amount}</td>
                      <td className="px-4 py-3 whitespace-nowrap text-sm">
                        <span
                          className={`inline-flex px-3 py-1 rounded-full text-xs font-semibold ${
                            payment.discounted
                              ? 'bg-green-100 text-green-700'
                              : 'bg-primary-100 text-primary-700'
                          }`}
                        >
                          {payment.discounted ? 'Discounted' : 'Standard'}
                        </span>
                      </td>
                      <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-500">
                        {new Date(payment.created_at).toLocaleString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        {/* User Management */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mt-12">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
            <div>
              <h2 className="text-2xl font-semibold text-gray-900">User Management</h2>
              <p className="text-sm text-gray-500 mt-1">View, update, or remove users across the platform.</p>
            </div>
            <button
              onClick={refreshUsers}
              className="px-5 py-2 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition"
            >
              Refresh List
            </button>
          </div>

          {(userActionMessage || userActionError) && (
            <div
              className={`mb-6 rounded-lg border px-4 py-3 text-sm ${
                userActionMessage
                  ? 'bg-green-50 border-green-200 text-green-700'
                  : 'bg-red-50 border-red-200 text-red-700'
              }`}
            >
              {userActionMessage || userActionError}
            </div>
          )}

          {users.length === 0 ? (
            <p className="text-gray-500">No users found.</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-100">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Name</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Email</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Role</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Attempts</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Payments</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Last Activity</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-100">
                  {users.map((item) => (
                    <tr key={item.id}>
                      <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                        <div className="flex items-center gap-2">
                          {item.is_admin && (
                            <span className="inline-flex items-center px-2 py-0.5 text-xs font-semibold rounded-full bg-primary-50 text-primary-700">
                              Admin
                            </span>
                          )}
                          {item.name}
                        </div>
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-600">{item.email}</td>
                      <td className="px-4 py-3 text-sm text-gray-600">{item.role}</td>
                      <td className="px-4 py-3 text-sm text-gray-600">
                        <div>
                          <span className="font-semibold text-gray-900">{item.attempts_passed}</span> / {item.attempts_total}
                        </div>
                        <div className="text-xs text-gray-400">Passed / Total</div>
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-600">
                        <div>
                          <span className="font-semibold text-gray-900">Rs. {item.payments_total_amount}</span>
                        </div>
                        <div className="text-xs text-gray-400">{item.payments_count} payments</div>
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-600">
                        <div>{item.last_attempt_at ? new Date(item.last_attempt_at).toLocaleDateString() : '—'}</div>
                        <div className="text-xs text-gray-400">
                          Pay: {item.last_payment_at ? new Date(item.last_payment_at).toLocaleDateString() : '—'}
                        </div>
                      </td>
                      <td className="px-4 py-3 text-sm">
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => handleEditClick(item)}
                            className="px-3 py-1.5 text-xs font-semibold text-white bg-primary-600 rounded-lg hover:bg-primary-700 transition"
                          >
                            Edit
                          </button>
                          <button
                            onClick={() => handleDeleteUser(item)}
                            className="px-3 py-1.5 text-xs font-semibold text-white bg-red-600 rounded-lg hover:bg-red-700 transition"
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>

      {editModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40 px-4">
          <div className="bg-white w-full max-w-lg rounded-2xl shadow-2xl p-8 relative">
            <button
              type="button"
              onClick={() => setEditModalOpen(false)}
              className="absolute top-4 right-4 text-gray-400 hover:text-gray-600"
              aria-label="Close edit modal"
            >
              <svg className="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>

            <h3 className="text-2xl font-semibold text-gray-900 mb-6">Edit User</h3>

            <form onSubmit={handleEditSubmit} className="space-y-5">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="edit-name">Full Name</label>
                <input
                  id="edit-name"
                  name="name"
                  type="text"
                  value={editForm.name}
                  onChange={handleEditChange}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="edit-email">Email</label>
                <input
                  id="edit-email"
                  name="email"
                  type="email"
                  value={editForm.email}
                  onChange={handleEditChange}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                  required
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1" htmlFor="edit-role">Role</label>
                  <input
                    id="edit-role"
                    name="role"
                    type="text"
                    value={editForm.role}
                    onChange={handleEditChange}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition"
                    required
                  />
                </div>
                <div className="flex items-center mt-6">
                  <input
                    id="edit-is-admin"
                    name="is_admin"
                    type="checkbox"
                    checked={editForm.is_admin}
                    onChange={handleEditChange}
                    className="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                  />
                  <label htmlFor="edit-is-admin" className="ml-2 text-sm text-gray-700">Grant admin access</label>
                </div>
              </div>

              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setEditModalOpen(false)}
                  className="px-5 py-2 rounded-lg border border-gray-300 text-gray-600 hover:bg-gray-100 transition"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={savingUser}
                  className="px-5 py-2 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {savingUser ? 'Saving...' : 'Save Changes'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminDashboard;

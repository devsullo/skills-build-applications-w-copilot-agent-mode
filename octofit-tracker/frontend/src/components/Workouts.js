import React, { useCallback, useEffect, useState } from 'react';

const Workouts = () => {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [showModal, setShowModal] = useState(false);

  const baseUrl = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
    : 'http://localhost:8000/api';
  const endpoint = `${baseUrl}/workouts/`;

  const fetchData = useCallback(() => {
    console.log('[Workouts] Fetch endpoint:', endpoint);

    fetch(endpoint)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('[Workouts] Fetched data:', data);
        const results = Array.isArray(data)
          ? data
          : Array.isArray(data?.results)
          ? data.results
          : [];
        setItems(results);
      })
      .catch((fetchError) => {
        console.error('[Workouts] Fetch error:', fetchError);
        setError(fetchError.message);
      });
  }, [endpoint]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const filteredItems = items.filter((item) => {
    const text = `${item.name || item.title || ''} ${item.duration || item.notes || ''}`.toLowerCase();
    return text.includes(searchTerm.toLowerCase());
  });

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-header d-flex justify-content-between align-items-center">
          <div>
            <h2 className="h4 mb-0">Workouts</h2>
            <p className="mb-0 text-muted">Review workout sessions delivered from the backend API.</p>
          </div>
          <div>
            <button type="button" className="btn btn-outline-primary btn-sm me-2" onClick={fetchData}>
              Refresh
            </button>
            <button type="button" className="btn btn-secondary btn-sm" onClick={() => setShowModal(true)}>
              View endpoint
            </button>
          </div>
        </div>
        <div className="card-body">
          <form className="row g-3 mb-3" onSubmit={(e) => e.preventDefault()}>
            <div className="col-md-6">
              <label htmlFor="workout-search" className="form-label">
                Search workouts
              </label>
              <input
                id="workout-search"
                type="text"
                className="form-control"
                placeholder="Filter by workout name, duration, or notes"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </form>

          <div className="mb-3">
            <a href={endpoint} className="link-primary" target="_blank" rel="noreferrer">
              Open backend endpoint in a new tab
            </a>
          </div>

          {error && <div className="alert alert-danger">{error}</div>}

          {items.length === 0 && !error ? (
            <div className="alert alert-info">Loading workouts...</div>
          ) : (
            <div className="table-responsive">
              <table className="table table-hover table-striped align-middle mb-0">
                <thead className="table-light">
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Workout</th>
                    <th scope="col">Duration / Notes</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredItems.map((item, index) => (
                    <tr key={item.id || index}>
                      <td>{index + 1}</td>
                      <td>{item.name || item.title || 'Unnamed workout'}</td>
                      <td>{item.duration || item.notes || JSON.stringify(item)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>

      {showModal && <div className="modal-backdrop-custom" onClick={() => setShowModal(false)} />}
      {showModal && (
        <div className="modal modal-custom d-block" tabIndex="-1" role="dialog">
          <div className="modal-dialog modal-dialog-centered" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Workouts API Endpoint</h5>
                <button type="button" className="btn-close" aria-label="Close" onClick={() => setShowModal(false)} />
              </div>
              <div className="modal-body">
                <p className="mb-2">Endpoint:</p>
                <pre className="bg-light p-3 rounded">{endpoint}</pre>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary btn-sm" onClick={() => setShowModal(false)}>
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Workouts;

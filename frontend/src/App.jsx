import React, { useState } from 'react';
import Landing from './components/Landing';
import Dashboard from './components/Dashboard';
import '../index.css';

function App() {
  const [view, setView] = useState('landing');

  return (
    <div className="App">
      <header className="container">
        <div className="logo" onClick={() => setView('landing')} style={{cursor: 'pointer'}}>
          <span>Trace</span>AI
        </div>
        <nav>
          <button className="btn btn-primary" onClick={() => setView('dashboard')}>
            {view === 'landing' ? 'Get Started' : 'Logout'}
          </button>
        </nav>
      </header>

      <main className="container">
        {view === 'landing' ? (
          <Landing onStart={() => setView('dashboard')} />
        ) : (
          <Dashboard />
        )}
      </main>

      <footer className="container" style={{marginTop: '4rem', padding: '2rem 0', textAlign: 'center', borderTop: '1px solid var(--border)'}}>
        <p style={{color: 'var(--text-muted)'}}>&copy; 2026 TraceAI. Premium Debugging Platform.</p>
      </footer>
    </div>
  );
}

export default App;

import React, { useState } from 'react';

const Dashboard = () => {
    const [errorLog, setErrorLog] = useState('');
    const [analyzing, setAnalyzing] = useState(false);
    const [result, setResult] = useState(null);
    const [repoPath, setRepoPath] = useState('');

    const handleIndex = async () => {
        if (!repoPath) return alert('Enter a project path');
        setAnalyzing(true);
        try {
            const resp = await fetch('http://localhost:8000/index', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ path: repoPath })
            });
            const data = await resp.json();
            alert(`Indexed ${data.indexed_chunks} chunks successfully!`);
        } catch (err) {
            alert('Failed to index project.');
        } finally {
            setAnalyzing(false);
        }
    };

    const handleAnalyze = async () => {
        if (!errorLog) return alert('Paste an error log first');
        setAnalyzing(true);
        setResult(null); // Clear previous results
        console.log("Starting analysis for:", errorLog);
        try {
            const resp = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ error_log: errorLog })
            });

            if (!resp.ok) {
                const errorData = await resp.json();
                console.error("Backend Error:", errorData);
                alert(`Analysis failed: ${errorData.detail || 'Unknown error'}`);
                return;
            }

            const data = await resp.json();
            console.log("Analysis Result received:", data);
            setResult(data);
        } catch (err) {
            console.error("Fetch Error:", err);
            alert('Analysis failed: Could not connect to backend server. Is it running on port 8000?');
        } finally {
            setAnalyzing(false);
        }
    };

    return (
        <div className="dashboard">
            <div className="glass-panel" style={{ padding: '1.5rem', marginBottom: '2rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
                <input
                    type="text"
                    placeholder="Enter local repository path..."
                    value={repoPath}
                    onChange={(e) => setRepoPath(e.target.value)}
                    style={{ flexGrow: 1, padding: '0.75rem', borderRadius: '0.5rem', background: 'rgba(0,0,0,0.3)', border: '1px solid var(--border)', color: 'white' }}
                />
                <button className="btn btn-primary" onClick={handleIndex} disabled={analyzing}>
                    {analyzing ? 'Indexing...' : 'Index Repo'}
                </button>
            </div>

            <div className="dashboard-grid">
                <div className="glass-panel panel">
                    <div className="panel-header">
                        <span>Runtime Error Log</span>
                        <button className="btn btn-primary" style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }} onClick={handleAnalyze} disabled={analyzing}>
                            {analyzing ? 'Analyzing...' : 'Run Diagnostics'}
                        </button>
                    </div>
                    <textarea
                        placeholder="Paste your terminal error or crash log here..."
                        value={errorLog}
                        onChange={(e) => setErrorLog(e.target.value)}
                    ></textarea>
                </div>

                <div className="glass-panel panel">
                    <div className="panel-header">AI Analysis Result</div>
                    <div style={{ overflowY: 'auto', flexGrow: 1 }}>
                        {!result ? (
                            <div style={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)' }}>
                                Ready for analysis...
                            </div>
                        ) : (
                            <div style={{ padding: '0.5rem' }}>
                                <div style={{ marginBottom: '1.5rem' }}>
                                    <label style={{ color: 'var(--primary)', fontSize: '0.8rem', fontWeight: 600 }}>ROOT CAUSE</label>
                                    <p style={{ fontSize: '1.1rem', fontWeight: 700 }}>{result.root_cause}</p>
                                </div>

                                <div style={{ marginBottom: '1.5rem' }}>
                                    <label style={{ color: 'var(--secondary)', fontSize: '0.8rem', fontWeight: 600 }}>EXPLANATION</label>
                                    <p style={{ color: 'var(--text-muted)' }}>{result.explanation}</p>
                                </div>

                                <div style={{ marginBottom: '1.5rem' }}>
                                    <label style={{ color: '#4ade80', fontSize: '0.8rem', fontWeight: 600 }}>SUGGESTED FIX</label>
                                    <div style={{ background: '#000', padding: '1rem', borderRadius: '0.5rem', fontFamily: 'Fira Code', fontSize: '0.9rem', marginTop: '0.5rem' }}>
                                        {result.suggested_fix}
                                    </div>
                                </div>

                                <div>
                                    <label style={{ color: 'var(--accent)', fontSize: '0.8rem', fontWeight: 600 }}>RELEVANT FILES</label>
                                    <ul style={{ listStyle: 'none', marginTop: '0.5rem', display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                                        {result.relevant_files?.map(f => (
                                            <li key={f} style={{ background: 'rgba(255,255,255,0.1)', padding: '0.2rem 0.6rem', borderRadius: '0.2rem', fontSize: '0.8rem' }}>
                                                {f}
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;

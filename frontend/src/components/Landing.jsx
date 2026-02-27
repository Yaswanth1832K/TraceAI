import React from 'react';

const Landing = ({ onStart }) => {
    return (
        <section className="hero">
            <h1>Decode Errors. Fast.</h1>
            <p className="subtitle">
                TraceAI analyzes your entire repository to find the root cause of bugs that traditional tools miss.
                Context-aware, AI-powered, and built for modern engineering teams.
            </p>

            <div style={{ marginTop: '3rem', display: 'flex', gap: '1rem' }}>
                <button className="btn btn-primary" onClick={onStart}>
                    Try it Now Free
                </button>
                <button className="btn" style={{ border: '1px solid var(--border)', color: 'var(--text-main)' }}>
                    View Demo
                </button>
            </div>

            <div className="glass-panel" style={{ marginTop: '5rem', width: '100%', height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative', overflow: 'hidden' }}>
                <div style={{
                    position: 'absolute',
                    width: '300px',
                    height: '300px',
                    background: 'var(--primary)',
                    filter: 'blur(100px)',
                    opacity: '0.2',
                    top: '10%'
                }}></div>
                <div style={{ fontFamily: 'Fira Code', textAlign: 'left', color: 'var(--primary)', padding: '2rem' }}>
                    <p>$ traceai analyze "Error: Cannot find module 'express'"</p>
                    <p style={{ color: 'var(--text-muted)' }}>Scanning repository...</p>
                    <p style={{ color: 'var(--secondary)' }}>Found missing dependency in package.json (Line 12)</p>
                    <p style={{ color: '#4ade80' }}>Resolution: npm install express</p>
                </div>
            </div>
        </section>
    );
};

export default Landing;

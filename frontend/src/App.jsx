import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('single');
  const [tone, setTone] = useState('Professional');
  const [goal, setGoal] = useState('Book a meeting');

  // Single Prospect State
  const [profile, setProfile] = useState('');
  const [singleResult, setSingleResult] = useState(null);
  const [singleLoading, setSingleLoading] = useState(false);
  const [singleError, setSingleError] = useState('');

  // Batch CSV State
  const [csvFile, setCsvFile] = useState(null);
  const [batchLoading, setBatchLoading] = useState(false);
  const [batchError, setBatchError] = useState('');
  const [csvDownloadUrl, setCsvDownloadUrl] = useState('');

  const handleGenerateSingle = async () => {
    if (!profile.trim()) {
      setSingleError("Please enter a prospect profile.");
      return;
    }
    setSingleError('');
    setSingleLoading(true);
    setSingleResult(null);

    try {
      const response = await axios.post('http://localhost:8000/api/generate', {
        profile, tone, goal
      });
      setSingleResult(response.data);
    } catch (err) {
      setSingleError("Error generating outreach: " + err.message);
    } finally {
      setSingleLoading(false);
    }
  };

  const handleGenerateBatch = async () => {
    if (!csvFile) {
      setBatchError("Please upload a CSV file.");
      return;
    }
    setBatchError('');
    setBatchLoading(true);
    setCsvDownloadUrl('');

    const formData = new FormData();
    formData.append('file', csvFile);
    formData.append('tone', tone);
    formData.append('goal', goal);

    try {
      const response = await axios.post('http://localhost:8000/api/generate-batch', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      if (response.data.error) {
        setBatchError(response.data.error);
      } else {
        // Create downloadable blob
        const blob = new Blob([response.data.csv_data], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        setCsvDownloadUrl(url);
      }
    } catch (err) {
      setBatchError("Error generating batch outreach: " + err.message);
    } finally {
      setBatchLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>✉️ Cold Outreach Personaliser</h1>
        <p>Generate personalised cold outreach emails using Gemini API.</p>
      </header>

      <div className="main-content">
        <aside className="sidebar">
          <h2>Outreach Settings</h2>
          <div className="input-group">
            <label>Select Tone</label>
            <select value={tone} onChange={(e) => setTone(e.target.value)}>
              <option>Professional</option>
              <option>Friendly</option>
              <option>Casual</option>
              <option>Bold</option>
            </select>
          </div>
          <div className="input-group">
            <label>Select Goal</label>
            <select value={goal} onChange={(e) => setGoal(e.target.value)}>
              <option>Book a meeting</option>
              <option>Introduce product</option>
              <option>Follow up</option>
              <option>Partnership</option>
              <option>Networking</option>
            </select>
          </div>
        </aside>

        <section className="content">
          <div className="tabs">
            <button 
              className={activeTab === 'single' ? 'active' : ''} 
              onClick={() => setActiveTab('single')}
            >
              👤 Single Prospect
            </button>
            <button 
              className={activeTab === 'batch' ? 'active' : ''} 
              onClick={() => setActiveTab('batch')}
            >
              📊 Batch CSV
            </button>
          </div>

          <div className="tab-content">
            {activeTab === 'single' && (
              <div className="single-prospect">
                <h2>Single Prospect</h2>
                <textarea 
                  placeholder="Example: Sarah is the Head of Marketing at Acme Technologies..."
                  value={profile}
                  onChange={(e) => setProfile(e.target.value)}
                  rows={8}
                ></textarea>
                {singleError && <div className="error">{singleError}</div>}
                
                <button className="primary-btn" onClick={handleGenerateSingle} disabled={singleLoading}>
                  {singleLoading ? "✨ Generating..." : "✨ Generate Outreach"}
                </button>

                {singleResult && (
                  <div className="result-container">
                    <div className="success-banner">Outreach generated!</div>
                    <div className="result-field">
                      <label>Subject</label>
                      <input type="text" readOnly value={singleResult.subject} />
                    </div>
                    <div className="result-field">
                      <label>Email</label>
                      <textarea readOnly value={singleResult.email} rows={10}></textarea>
                    </div>
                    <div className="result-field">
                      <label>Follow-up</label>
                      <textarea readOnly value={singleResult.followup} rows={6}></textarea>
                    </div>
                  </div>
                )}
              </div>
            )}

            {activeTab === 'batch' && (
              <div className="batch-prospect">
                <h2>Batch CSV</h2>
                <p className="info-box">Your CSV must contain a column named 'profile'.</p>
                
                <div className="file-uploader">
                  <input 
                    type="file" 
                    accept=".csv"
                    onChange={(e) => setCsvFile(e.target.files[0])} 
                  />
                </div>

                {batchError && <div className="error">{batchError}</div>}
                
                <button 
                  className="primary-btn" 
                  onClick={handleGenerateBatch} 
                  disabled={batchLoading || !csvFile}
                >
                  {batchLoading ? "🚀 Generating..." : "🚀 Generate Batch Outreach"}
                </button>

                {csvDownloadUrl && (
                  <div className="result-container">
                    <div className="success-banner">Batch generation completed!</div>
                    <a href={csvDownloadUrl} download="personalised_outreach.csv" className="download-btn">
                      ⬇️ Download CSV
                    </a>
                  </div>
                )}
              </div>
            )}
          </div>
        </section>
      </div>
    </div>
  );
}

export default App;

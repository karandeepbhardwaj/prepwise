import { useState } from 'react';
import { UrlParser } from './url-parser';
import { GuidePreview } from './guide-preview';
import { submitPrepRequest } from '../lib/api';

export function PrepForm() {
  const [title, setTitle] = useState('');
  const [responsibilities, setResponsibilities] = useState('');
  const [jobUrl, setJobUrl] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<unknown>(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true); setError('');
    try {
      const data = await submitPrepRequest({ position_title: title, responsibilities, job_url: jobUrl || undefined, email });
      setResult(data.guide);
    } catch (err) { setError(err instanceof Error ? err.message : 'Something went wrong'); }
    finally { setLoading(false); }
  };

  return (<div className="prep-form-container">
    <form onSubmit={handleSubmit} className="prep-form">
      <div className="form-group"><label>Position Title</label><input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="e.g. Senior Software Engineer" required /></div>
      <UrlParser value={jobUrl} onChange={setJobUrl} onParsed={(t, r) => { if (t) setTitle(t); if (r) setResponsibilities(r); }} />
      <div className="form-group"><label>Responsibilities / Job Description</label><textarea value={responsibilities} onChange={e => setResponsibilities(e.target.value)} rows={6} placeholder="Paste job description or key responsibilities..." /></div>
      <div className="form-group"><label>Your Email</label><input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="guide@example.com" required /></div>
      <button type="submit" className="btn-submit" disabled={loading}>{loading ? 'Generating guide...' : 'Generate Prep Guide'}</button>
      {error && <p className="error">{error}</p>}
    </form>
    {result && <GuidePreview guide={result} />}
  </div>);
}

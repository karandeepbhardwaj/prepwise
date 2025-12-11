import { useState } from 'react';
import { parseJobUrl } from '../lib/api';

interface Props { value: string; onChange: (url: string) => void; onParsed: (title: string, content: string) => void; }

export function UrlParser({ value, onChange, onParsed }: Props) {
  const [parsing, setParsing] = useState(false);
  const handleParse = async () => {
    if (!value) return;
    setParsing(true);
    try {
      const data = await parseJobUrl(value);
      onParsed(data.title, data.content);
    } catch { /* ignore */ }
    finally { setParsing(false); }
  };
  return (<div className="form-group"><label>Job Posting URL (optional)</label>
    <div className="url-input-group"><input type="url" value={value} onChange={e => onChange(e.target.value)} placeholder="https://linkedin.com/jobs/..." />
    <button type="button" onClick={handleParse} disabled={parsing || !value} className="btn-parse">{parsing ? 'Parsing...' : 'Parse'}</button></div></div>);
}

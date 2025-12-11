const API = '';
export async function submitPrepRequest(data: { position_title: string; responsibilities: string; job_url?: string; email: string }) {
  const res = await fetch(`${API}/api/prepare`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
  if (!res.ok) throw new Error((await res.json()).detail ?? 'Request failed');
  return res.json();
}
export async function parseJobUrl(url: string) {
  const res = await fetch(`${API}/api/parse-url`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ url }) });
  if (!res.ok) throw new Error('Failed to parse URL');
  return res.json();
}

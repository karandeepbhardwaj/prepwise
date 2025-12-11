interface Props { steps: { name: string; status: 'pending' | 'active' | 'done' }[]; }
export function ProgressTracker({ steps }: Props) {
  return (<div className="progress-tracker">{steps.map((step, i) => (
    <div key={i} className={`progress-step ${step.status}`}><span className="step-dot" /><span>{step.name}</span></div>
  ))}</div>);
}

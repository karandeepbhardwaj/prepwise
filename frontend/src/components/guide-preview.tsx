export function GuidePreview({ guide }: { guide: unknown }) {
  const g = guide as Record<string, unknown>;
  return (<div className="guide-preview"><h2>Guide Generated!</h2><p>A comprehensive interview prep guide for <strong>{g.position_title as string}</strong> has been sent to your email.</p>
    <div className="guide-stats"><div className="stat"><strong>{(g.questions as unknown[])?.length ?? 0}</strong><span>Questions</span></div>
    <div className="stat"><strong>{(g.technical_topics as unknown[])?.length ?? 0}</strong><span>Study Topics</span></div>
    <div className="stat"><strong>{(g.answer_frameworks as unknown[])?.length ?? 0}</strong><span>STAR Frameworks</span></div></div></div>);
}


type Props = {
  params: Promise<{ teamId: string }>;
};

export default async function TeamPage({ params }: Props) {
  const {teamId} = await params;
  return (
    <main style={{ padding: 24 }}>
      <h1>Team: {teamId}</h1>
      <p>Team analytics coming soon.</p>
      
    </main>
  );
}


type Props = {
  params: { teamId: string };
};

export default function TeamPage({ params }: Props) {
  console.log(params.teamId)
  return (
    <main style={{ padding: 24 }}>
      <h1>Team: {params.teamId}</h1>
      <p>Team analytics coming soon.</p>
      
    </main>
  );
}

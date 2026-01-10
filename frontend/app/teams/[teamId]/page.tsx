
type Props = {
  params: Promise<{ teamId: string }>;
};

export default async function TeamPage({ params }: Props) {
  const {teamId} = await params;
  const [teamRes, statsRes] = await Promise.all([
    fetch(`http://localhost:8000/teams`),
    fetch(`http://localhost:8000/team-stats/${teamId}`),
  ]);

const teams = await teamRes.json();
const stats = await statsRes.json();

const team = teams.find((t: any) => t.team_id === teamId);
  return (
    <main style={{ padding: 24 }}>
      <h1>Team: {team?.team_name}</h1>
      <div>Wins: {stats?.wins}</div>
      <div>Losses: {stats?.losses}</div>
      <div>Points Per Game: {stats?.points_per_game}</div>
      <div>Rebounds Per Game: {stats?.rebounds_per_game}</div>
      <div>Assists Per Game: {stats?.assists_per_game}</div>
      {/* This is what needs to be edited to create the team page */}
    </main>
  );
}

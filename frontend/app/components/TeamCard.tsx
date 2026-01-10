type Team = {
  id: string;
  name: string;
  abbr: string;
};

type Props = {
  team: Team;
  onSelect: (teamId: string) => void;
};

export default function TeamCard({ team, onSelect }: Props) {
  return (
    <button className="card" onClick={() => onSelect(team.id)}>
      <div className="cardTop">
        <div className="abbr">{team.abbr}</div>
        <div className="chev">→</div>
      </div>

      <div className="name">{team.name}</div>
      <div className="hint">View analytics</div>

      <div className="cardGlow" aria-hidden="true" />
    </button>
  );
}

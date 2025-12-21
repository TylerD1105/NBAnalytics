"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

const TEAMS = [
  { id: "ATL", name: "Atlanta Hawks" },
  { id: "BOS", name: "Boston Celtics" },
  { id: "LAL", name: "Los Angeles Lakers" },
  { id: "GSW", name: "Golden State Warriors" },
];

export default function HomePage() {
  const router = useRouter();
  const [teamId, setTeamId] = useState("");

  return (
    <main style={{ padding: 24 }}>
      <h1>NBA Analytics</h1>

      <select
        value={teamId}
        onChange={(e) => setTeamId(e.target.value)}
      >
        <option value="">Select a team</option>
        {TEAMS.map((team) => (
          <option key={team.id} value={team.id}>
            {team.name}
          </option>
        ))}
      </select>

      <button
        disabled={!teamId}
        onClick={() => router.push(`/teams/${teamId}`)}
      >
        View Team
      </button>
    </main>
  );
}

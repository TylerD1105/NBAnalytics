"use client";

import { useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import SwipeCarousel from "../components/SwipeCarousel/SwipeCarousel";

type Team = {
  id: string;
  name: string;
  abbr: string;
};

export default function HomePage() {
  const router = useRouter();
  const [query, setQuery] = useState("");




  return (
    <main className="page">
      <div className="bgGlow" aria-hidden="true" />

      <header className="header">
        <div className="brand">
          <div className="logoMark" aria-hidden="true">
            <span />
          </div>

          <div>
            <h1 className="title">NBA Analytics</h1>
            <p className="subtitle">
              Pick a team to view current season dashboards and player analytics.
            </p>
          </div>
        </div>

        <div className="searchRow">
          <div className="searchWrap">
            <span className="searchIcon" aria-hidden="true">
              ⌕
            </span>
            <input
              className="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search teams (e.g., Lakers, BOS, OKC)…"
              aria-label="Search teams"
            />
          </div>

          <div className="pill">
            <span className="pillDot" aria-hidden="true" />
          </div>
        </div>
      </header>

      <section className="grid" aria-label="Team selection grid">
        <SwipeCarousel />
      </section>

      <footer className="footer">
        <span className="footerMuted">
          Frontend-only MVP. Data will be wired in later.
        </span>
      </footer>
    </main>
  );
}

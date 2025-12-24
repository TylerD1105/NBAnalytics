"use client";
import React, { useEffect, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import styles from './SwipeCarousel.module.css';3

const imgs = [
    "/images/ATL.png",
    "/images/BOS.png",
    "/images/BRK.png",
];

type Team = {
    team_id: string;
    team_name: string;
    team_abbreviation: string;
    image_url: string;
}

export default function SwipeCarousel() {
    const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, skipSnaps: true });
    const [teams, setTeams] = useState<Team[]>([]);

    useEffect(() => {
        fetch('http://localhost:8000/teams')
            .then(response => response.json())
            .then(data => setTeams(data))
            .catch(error => console.error('Error fetching teams:', error));
    }, [])


    useEffect(() => {
    if (emblaApi) {
      console.log(emblaApi.slideNodes()) // Access API
    }
    }, [emblaApi])

    return (
        <div className = {styles.embla} ref={emblaRef}>
            <div className={styles.embla__container}>
                {teams.map((team, index) => (
                    <div className = {styles.embla__slide} key = {index}>
                        <img src = {team.image_url} alt = {team.team_name}></img>
                    </div>
                ))}

                </div>
            </div>

    );

}
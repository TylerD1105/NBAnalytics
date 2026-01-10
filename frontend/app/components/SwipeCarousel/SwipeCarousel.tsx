"use client";
import React, { useEffect, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import styles from './SwipeCarousel.module.css';
import { useRouter } from "next/navigation";



type Team = {
    team_id: string;
    team_name: string;
    team_abbreviation: string;
    image_url: string;
}
//TODO: Make function that will call the embla API and based on which index is centered in the viewpoint, have index + 1 and index - 1 scale and animate to get bigger once it goes more towards the center?


export default function SwipeCarousel() {
    const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, skipSnaps: true });
    const [teams, setTeams] = useState<Team[]>([]);
    const router = useRouter();

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
                    <div className = {styles.embla__slide} key = {index} onClick = {() => {
                        router.push(`teams/${team.team_id}`)
                    }}>
                        <img src = {team.image_url} alt = {team.team_name}></img>
                        
                    </div>
                ))}

                </div>
            </div>

    );

}
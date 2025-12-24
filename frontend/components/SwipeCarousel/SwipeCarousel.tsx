"use client";
import React, { useEffect, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import styles from './SwipeCarousel.module.css';3

const imgs = [
    "/images/ATL.png",
    "/images/BOS.png",
    "/images/BRK.png",
];

export default function SwipeCarousel() {
    const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, skipSnaps: true });

    useEffect(() => {
    if (emblaApi) {
      console.log(emblaApi.slideNodes()) // Access API
    }
    }, [emblaApi])

    return (
        <div className = {styles.embla} ref={emblaRef}>
            <div className={styles.embla__container}>
                {imgs.map((img, idx) => (
                    //TODO: Update alt text to link the img to the database entry for each so we can have names for teams as alt text instead of slide 1
                    <div className = {styles.embla__slide} key={idx}>
                        <img src={img} alt = {"Slide " + (idx + 1)}></img>
                    </div>
                ))}

                </div>
            </div>

    );

}
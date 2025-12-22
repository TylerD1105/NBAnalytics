"use client";
import React, { useEffect, useState } from "react";
import { motion, useMotionValue } from "framer-motion";

const imgs = [
    "/images/ATL.png",
    "/images/BOS.png",
    "/images/NETS.png",
];

const SPRING_OPTIONS = {
                    type: "spring" as const,
                    mass: 3,
                    stiffness: 400,
                    damping: 50,
                };
const DRAG_BUFFER = 150;
const AUTO_DELAY = 10000; //10 seconds
export const SwipeCarousel = () => {
    const [dragging, setDragging] = useState(false);
    const [imgIndex, setImgIndex] = useState(0);

    useEffect(() => {
        const intervalRef = setInterval(() => {
            //function to do smth
        }, AUTO_DELAY);
        return () => clearInterval(intervalRef);
    }, [])

    const dragX = useMotionValue(0);

    const onDragStart = () => {
        setDragging(true);
    }

    const onDragEnd = () => {
        setDragging(false);

        const x = dragX.get();

        if (x <= -DRAG_BUFFER && imgIndex < imgs.length - 1) {
            setImgIndex((pv) => pv + 1);
        }else if (x >= DRAG_BUFFER && imgIndex > 0) {
            setImgIndex((pv) => pv - 1);
        }
    };
return <div
    className="relative min-h-screen overflow-hidden bg-neutral-950 py-8">
            <motion.div
            drag = "x"
            dragConstraints = {{
                left: 0,
                right: 0,
            }}
            style = {{
                x: dragX,
            }}
            animate = {{
                translateX: `-${imgIndex * 100}%`,
            }}
            transition = {SPRING_OPTIONS}
            onDragStart={onDragStart}
            onDragEnd = {onDragEnd}
            className = "flex items-center cursor-grab active:cursor-grabbing">
            <Images imgIndex={imgIndex}/>
            </motion.div>
            <Dots imgIndex={imgIndex} setImgIndex={setImgIndex} />    
      </div>

};

const Images = ({ imgIndex }: { imgIndex: number }) => {
    return (
        <>  
            {imgs.map((imgSrc, idx) => {
                return (
                <motion.div 
                key={idx}
                style = {{
                    backgroundImage : `url(${imgSrc})`,
                    backgroundSize : `cover`,
                    backgroundPosition : `center`,
                }}
                animate = {{
                    scale: imgIndex === idx ? 0.95 : 0.85,
                }}
                transition = {SPRING_OPTIONS}
                className="aspect-video w-screen shrink-0 rounded-xl bg-neutral-800 object-cover"
                />
            );
            })}
        </>
    );
};
//In future do not use dots since it will be 30 teams, instead have a search function that will slide to that team
const Dots = ({ imgIndex , setImgIndex } : { imgIndex: number; setImgIndex: React.Dispatch<React.SetStateAction<number>> }) => {
    return <div
    className="mt-4 flex w-full justify-center gap-2">
        {imgs.map((img, idx) => {
            return <button
            key = {idx}
            onClick={() => setImgIndex(idx)}
            className = {`h-3 w-3 rounded-full transition-colors ${
                idx === imgIndex ? "bg-neutral-50":"bg-neutral-500"}`}
            />
        })}
    </div>;

};
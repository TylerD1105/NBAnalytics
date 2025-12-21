import React, { useState } from "react";
import { motion, useMotionValue } from "framer-motion";
const imgs = [
    "/images/ATL.png",
    "/images/BOS.png",
    "/images/NETS.png",
];

export const SwipeCarousel = () => {
    const [dragging, setDragging] = useState(false);
    const [imgIndex, setImgIndex] = useState(0);

    const dragX = useMotionValue(0);

    const onDragStart = () => {
        setDragging(true);
    }

    const onDragEnd = () => {
        setDragging(false);
    }
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
                translateX: `-${imgIndex * 100}`,
            }}
            onDragStart={onDragStart}
            onDragEnd = {onDragEnd}
            className = "flex items-center cursor-grab active:cursor-grabbing">
            <Images />
            </motion.div>    
      </div>

};

const Images = () => {
    return (
        <>  
            {imgs.map((imgSrc, idx) => {
                return (
                <div 
                key={idx}
                style = {{
                    backgroundImage : `url(${imgSrc})`,
                    backgroundSize : `cover`,
                    backgroundPosition : `center`,
                }} 
                className="aspect-video w-screen shrink-0 rounded-xl bg-neutral-800 object-cover"
                />
            );
            })}
        </>
    );
};
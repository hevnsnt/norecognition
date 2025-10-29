# **👾 Anti-Facial Recognition Pattern Generators (patterns.py)**

This module contains a comprehensive library of procedural and image-based pattern generators designed to create disruptive, obfuscating, and adversarial camouflage masks. These patterns leverage high-contrast geometry, visual saliency attacks, color space manipulation, and perceptual glitches, and are highly optimized using NumPy, Numba, CuPy, and MLX backends.

## **1\. Structural & Biometric Attacks**

These patterns directly target the features and processes used by facial recognition systems, including key biometric landmarks and depth/IR capture mechanisms.

| Key | Description | Technique |
| :---- | :---- | :---- |
| faceid\_structured\_light | Simulated Apple Face ID Structured Light. Projects a dense grid of simulated IR dots. Supports Full mode (entire face, pre-mask behavior) and Mask mode (focused on periocular region, post-iOS 15.4 behavior). Optimized for high-density coordinate generation on GPU/Numba. | Structured Light Simulation, Hardware Attack, Biometric |
| hyperface\_like | Generates a high-contrast, blocky Hyperface-style pattern using geometric shapes or lines, often incorporating concentric circles over detected features (eyes, mouth). | Structural, Geometric, Landmark-Based |
| dazzle\_surgical\_lines | Draws thick, high-contrast lines connecting key facial landmarks (eyes, nose, brows, cheeks) to visually break up feature continuity, inspired by surgical marking guides. | Landmark Disruption, CV Dazzle |
| key\_feature\_blackout | Applies solid black or white censor bars/patches specifically over the eyes and mouth using detected bounding boxes for maximum feature obscuration. | Negative Space, Feature Attack |
| saliency\_eye\_attack | Densely stamps or tiles random eye features across the entire mask area, overloading the recognition system's saliency map and feature extractors. | Saliency Attack, Feature Overload |
| ir\_led\_attack | Simulates the blinding effect (glare and bloom) caused by a cluster of bright Infrared LEDs, designed to disrupt IR-based depth sensors. This is a basic attack compared to faceid\_structured\_light | Sensor Attack, IR Simulation |

## **2\. Geometric & Noise Attacks**

These patterns rely on creating visual chaos through noise, repetition, and high-contrast, non-organic structures.

| Key | Description | Technique |
| :---- | :---- | :---- |
| simple\_shapes | Overlays random simple geometric shapes (circles, squares, lines, triangles) in various colors and thicknesses. | Geometric, Chaos |
| fractal\_noise | Generates colorful, complex Mandelbrot/Julia set-like fractal patterns over the mask area. | Algorithmic, Noise |
| perlin\_noise | Generates smooth, organic Perlin noise patterns, colored using random OpenCV colormaps. | Algorithmic, Noise |
| hf\_noise | Applies simple, high-frequency static (white noise/random pixels) for general disruption. | Noise, High-Frequency |
| checkerboard | Generates a high-contrast black and white checkerboard pattern, known to generate Moire effects on certain sensors. | Geometric, Interference |
| gradient | Applies a smooth, linear color gradient (horizontal or vertical) for simple tonal shifting. | Tonal, Simple |
| op\_art\_chevrons | Generates a repeating, high-contrast optical art pattern using V-shapes or chevrons to create visual tension and movement. | Optical Illusion, Geometric |
| tiled\_logo | Tiles a consistent, high-contrast geometric logo (bullseye, crosshairs, chevron) across the mask. | Geometric, Repetition |
| fft\_noise | Modifies the image in the frequency domain (FFT) by enhancing low or high frequencies to create a unique, distorted noise texture. | Spectral, Algorithmic |
| simulated\_optimized\_noise | Generates posterized Perlin noise and colors it with specific color maps, simulating output of optimized adversarial noise algorithms. | Adversarial, Noise |

## **3\. Glitch & Distortion Attacks**

These patterns aim to confuse algorithms by warping, shifting, or corrupting the input image data.

| Key | Description | Technique |
| :---- | :---- | :---- |
| vortex | Applies a twisting, circular distortion to the mask area, rotating pixels around a central point. | Warping, Glitch |
| optical\_flow | Uses optical flow algorithms (Farneback) to calculate movement between two slightly transformed versions of the image, then applies that calculated flow as a liquify/warp effect. | Warping, Glitch |
| photonegative\_patch | Inverts the colors (photonegative effect) only within the masked area. | Tonal, Color Space Attack |
| colorspace\_jitter | Creates high-frequency random noise strictly within the Cr/Cb (chrominance) channels, leaving the Y (luma) channel mostly untouched. | Color Space Attack |
| selective\_blur | Applies patches of extreme Gaussian blur over random mask regions to locally destroy high-frequency detail. | Obfuscation, Feature Destruction |
| pixel\_sort\_glitch | Sorts pixel brightness values along random horizontal lines within the mask area, creating a popular digital glitch art effect. | Glitch, Corruption |
| rgb\_channel\_shift | Shifts the Red and Blue color channels by a random offset relative to the Green channel, resulting in severe color fringing. | Color Space Attack, Glitch |

## **4\. Feature and Landmark Disruption**

These techniques use features, landmarks, or adversarial elements to break feature detection pipelines.

| Key | Description | Technique |
| :---- | :---- | :---- |
| feature\_collage | Stamps and overlays random facial features (eyes, mouths, noses) sourced from external images across the mask area. | Feature Overload, Feature Attack |
| recursive\_face\_tile | Tiles the user's *own* detected face as a repeating pattern across the larger mask area. | Feature Overload, Repetition |
| swapped\_landmarks | Extracts and swaps key facial features (e.g., mouth pasted over an eye) to create biologically impossible feature geometry. | Landmark Disruption, Structural |
| landmark\_noise | Applies a patch of noise or blur only around a small radius of key detected facial landmarks (eyes, nose, mouth corners). | Targeted Obfuscation |
| adversarial\_patch | Places a single, small, randomly generated checkerboard/noise "sticker" over a key anchor point (e.g., nose tip, cheek). | Targeted Adversarial Attack |
| adversarial\_patch\_multi | Places multiple small, randomly generated adversarial patches over several key anchor points (eyes, nose, cheeks). | Multi-Targeted Adversarial Attack |

## **5\. Texture & Text/Symbolic Attacks**

These patterns incorporate recognizable symbols, dense text, or complex textures.

| Key | Description | Technique |
| :---- | :---- | :---- |
| camouflage | Tiles an external camouflage texture (loaded from workers) seamlessly across the mask. | Texture, Obfuscation |
| repeating\_texture\_object | Tiles a small, user-uploaded image (like a logo or object) repeatedly, with random scaling and jitter. | Texture, Repetition |
| warped\_face | Warps a user-uploaded image of a face using sin/cos waves and maps it to the mask area. | Texture, Distortion |
| pop\_art\_collage | Creates a collage using abstract line art and shapes, layered over a vibrant, multi-colored background. | Texture, Stylistic |
| random\_text | Overlays dense, randomly generated alphanumeric strings across the mask. | Symbolic, Noise |
| qr\_code | Tiles a randomly generated QR code pattern across the masked area. | Symbolic, Structural |
| ascii\_face | Stamps simplified faces constructed from ASCII characters (e.g., (o\_O)). | Symbolic, Text |
| trypophobia | Generates a pattern of dense, high-contrast circular "holes." | Psychological, Geometric |
| animal\_print | Procedurally generates a realistic animal print (e.g., leopard/jaguar rosettes). | Texture |


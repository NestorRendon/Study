[Stable Diffusion is a generative artificial intelligence (generative AI)](https://aws.amazon.com/ai/generative-ai/) model that produces unique photorealistic images from text messages and images. It was originally launched in 2022. In addition to images, the model can also be used to create videos and animations. The model is based on diffusion technology and uses latent space. This significantly reduces processing requirements, and the model can run on desktops or laptops equipped with GPUs. Stable Diffusion can be optimized to meet specific needs with as few as five images using inductive learning


Diffusion models for sound are ==advanced AI systems that create, clean, or change audio by reversing a step-by-step noise process==. They start with random static and slowly shape it into realistic music, speech, or sound effects. [[1](https://towardsdatascience.com/audio-diffusion-generative-musics-secret-sauce-f625d0aca800/), [2](https://www.emergentmind.com/topics/diffusion-based-sound-synthesis-model)]

How Audio Diffusion Works

- **Forward pass:** The system takes a clean sound and adds white noise step-by-step until it becomes pure static.

- **Reverse pass:** A neural network learns to do the opposite, removing the static bit by bit to recover or generate a clean audio signal.

- **Representation:** Sounds are often processed as 2D pictures called _mel spectrograms_ (showing time and frequency) or compressed in a latent space for faster, higher-quality results.

- **Vocoders:** Once the model generates a clean spectrogram, a neural vocoder (like HiFi-GAN) turns it back into an audible waveform
interface VideoPlayerElements {
    videoPlayer: HTMLVideoElement;
    playButton: HTMLButtonElement;
    stopButton: HTMLButtonElement;
}

interface VideoPlayerProtocol {
    playToggle(): void;
    stop(): void;
    startEvents(): void;
}

export default class VideoPlayer implements VideoPlayerProtocol {
    private videoPlayer: HTMLVideoElement;
    private playButton: HTMLButtonElement;
    private stopButton: HTMLButtonElement;

    constructor(videoPLayerElement: VideoPlayerElements) {
        this.videoPlayer = videoPLayerElement.videoPlayer;
        this.playButton = videoPLayerElement.playButton;
        this.stopButton = videoPLayerElement.stopButton;
    }

    startEvents(): void {
        throw new Error('Method not implemented.');
    }
    playToggle(): void {
        throw new Error('Method not implemented.');
    }
    stop(): void {
        throw new Error('Method not implemented.');
    }
}

const videoPlayer = new VideoPlayer({
    videoPlayer: document.querySelector('video') as HTMLVideoElement,
    playButton: document.querySelector('button') as HTMLButtonElement,
    stopButton: document.querySelector('button') as HTMLButtonElement,
});
videoPlayer.startEvents();

// Init & load audio file
document.addEventListener('DOMContentLoaded', function() {
    let wavesurfer = WaveSurfer.create({
        container: document.querySelector('#waveform'),
        waveColor: '#A8DBA8',
        progressColor: '#3B8686',
        backend: 'MediaElement',
        // your other options here
        plugins: [
            WaveSurfer.regions.create({
                regionsMinLength: 1,
                regions: [
                    {
                        start: 1,
                        end: 3,
                        loop: false,
                        color: 'hsla(400, 100%, 30%, 0.5)'
                    }, {
                        start: 5,
                        end: 7,
                        loop: false,
                        color: 'hsla(200, 50%, 70%, 0.4)',
                        minLength: 1,
                    }
                ],
                dragSelection: {
                    slop: 5
                }
            }),
    	]
    	});
    
    wavesurfer.load('http://localhost:8000/%E9%9F%B3%E6%AA%94/1737/0/52.565333333333335/audio.wav');

    // Play button
    let button = document.querySelector('#hongsang');

    button.addEventListener('click', (e) => {
        e.preventDefault();
        wavesurfer.playPause.bind(wavesurfer)();
    });
});


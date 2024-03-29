// Init & load audio file
document.addEventListener('DOMContentLoaded', function() {
    let container = django.jQuery("#waveform");
    let tok = container.data('tok');
    console.log(container.data('tok'))
    if(!tok)
        return;
    let regions = tok.map((sikan)=>({
        start: sikan[0],
        end: sikan[1],
        loop: false,
        color: 'hsla(400, 100%, 30%, 0.5)'
    }))
    console.log(regions)
    window.wavesurfer = WaveSurfer.create({
        container: document.querySelector('#waveform'),
        waveColor: '#A8DBA8',
        progressColor: '#3B8686',
        backend: 'MediaElement',
        // your other options here
        plugins: [
            WaveSurfer.regions.create({
                regionsMinLength: 1,
                regions: regions,
                dragSelection: {
                    slop: 5
                }
            }),
    	]
    	});
    
    window.wavesurfer.load(container.data('src'));

    // Play button
    let button = document.querySelector('#hongsang');

    button.addEventListener('click', (e) => {
        e.preventDefault();
        wavesurfer.playPause.bind(wavesurfer)();
    });
});


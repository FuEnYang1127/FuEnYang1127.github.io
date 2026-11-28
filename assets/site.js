/* Progressive publication filters and video playback; all papers remain available without JavaScript. */
(() => {
  'use strict';
  const visitorImage = document.querySelector('.visitor-map img');
  if (visitorImage) {
    const hideUnavailableMap = () => { visitorImage.closest('.visitor-section').hidden = true; };
    visitorImage.addEventListener('error', hideUnavailableMap);
    if (visitorImage.complete && !visitorImage.naturalWidth) hideUnavailableMap();
  }
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const states = [];
  const canAutoPlay = () => !reducedMotion.matches && !navigator.connection?.saveData;
  const setPlaying = (state, playing) => {
    state.stage.classList.toggle('is-playing', playing);
    state.button.textContent = playing ? 'Pause demo' : 'Play demo';
    state.button.setAttribute('aria-pressed', String(playing));
    state.button.setAttribute('aria-label', `${playing ? 'Pause' : 'Play'} demo for ${state.title}`);
  };
  const play = async state => {
    if (state.article.hidden) return;
    state.wantsPlayback = true;
    if (!state.video.src) {
      state.video.src = state.video.dataset.src;
      state.video.load();
    }
    try {
      await state.video.play();
      if (!state.wantsPlayback) state.video.pause();
      setPlaying(state, !state.video.paused);
    } catch {
      // Keep the static poster when autoplay or video loading is unavailable.
      setPlaying(state, false);
    }
  };
  const pause = state => {
    state.wantsPlayback = false;
    state.video.pause();
    setPlaying(state, false);
  };
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const state = states.find(item => item.video === entry.target);
      state.visible = entry.isIntersecting && !state.article.hidden;
      if (state.visible && !state.userPaused && canAutoPlay() && !document.hidden) play(state);
      else pause(state);
    });
  }, { threshold: .25 });
  document.querySelectorAll('.demo-video').forEach(video => {
    const figure = video.closest('figure');
    const state = { video, article: video.closest('.publication'), stage: video.parentElement, button: figure.querySelector('.demo-toggle'),
      title: video.closest('.publication').querySelector('h3').textContent,
      userPaused: false, visible: false };
    states.push(state);
    state.button.hidden = false;
    state.button.addEventListener('click', () => {
      if (video.paused) { state.userPaused = false; play(state); }
      else { state.userPaused = true; pause(state); }
    });
    video.addEventListener('error', () => { pause(state); state.button.textContent = 'Demo unavailable'; state.button.disabled = true; });
    observer.observe(video);
  });
  const filters = document.querySelector('.publication-filters');
  const papers = Array.from(document.querySelectorAll('.publication'));
  const filterStatus = document.querySelector('#publication-filter-status');
  if (filters && papers.length) {
    const buttons = Array.from(filters.querySelectorAll('[data-filter]'));
    const applyFilter = category => {
      papers.forEach(paper => {
        paper.hidden = category !== 'all' && paper.dataset.category !== category;
      });
      buttons.forEach(button => {
        button.setAttribute('aria-pressed', String(button.dataset.filter === category));
      });
      states.forEach(state => {
        if (state.article.hidden) { state.visible = false; pause(state); }
      });
      const count = papers.filter(paper => !paper.hidden).length;
      filterStatus.textContent = `${count} publications shown.`;
    };
    buttons.forEach(button => {
      button.addEventListener('click', () => applyFilter(button.dataset.filter));
    });
    // Reveal a paper reached through a direct anchor even if a filter hid it.
    window.addEventListener('hashchange', () => {
      let id;
      try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
      const paper = document.getElementById(id)?.closest('.publication');
      if (paper?.hidden) {
        applyFilter('all');
        paper.scrollIntoView({ block: 'start', behavior: 'auto' });
      }
    });
    filters.hidden = false;
  }
  document.addEventListener('visibilitychange', () => {
    states.forEach(state => {
      if (document.hidden) pause(state);
      else if (state.visible && !state.userPaused && canAutoPlay()) play(state);
    });
  });
  reducedMotion.addEventListener('change', () => {
    states.forEach(state => {
      if (!canAutoPlay()) pause(state);
      else if (state.visible && !state.userPaused && !document.hidden) play(state);
    });
  });
})();

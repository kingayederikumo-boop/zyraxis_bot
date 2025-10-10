// basic client to call backend endpoints (uses DEMO_TELEGRAM_ID for testing)
async function q(url){ let r = await fetch(url); if(!r.ok) return null; return r.json(); }

document.addEventListener('DOMContentLoaded', async ()=>{
  const h = document.getElementById('historyList');
  const imgs = document.getElementById('imagesList');
  const profileBtn = document.getElementById('profileBtn');
  const modal = document.getElementById('profileModal');
  document.getElementById('closeProfile').onclick = ()=> modal.classList.add('hidden');

  load();
  async function load(){
    h.innerHTML = 'Loading...'; imgs.innerHTML = 'Loading...';
    const history = await q('/api/history') || [];
    const images = await q('/api/images') || [];
    h.innerHTML = history.map(x=>`<div class="card"><strong>${escapeHtml(x.prompt)}</strong><div>${escapeHtml(x.response)}</div><small>${x.created_at}</small></div>`).join('') || '<em>No history</em>';
    imgs.innerHTML = images.map(x=>`<div class="card"><img src="${x.url}" style="width:100%;"><small>${escapeHtml(x.prompt)}</small></div>`).join('') || '<em>No images</em>';
  }

  profileBtn.onclick = ()=> modal.classList.remove('hidden');
  document.getElementById('delete').onclick = async ()=>{
    if(!confirm('Delete account and clear subscriptions?')) return;
    await fetch('/api/delete_account',{method:'POST'});
    alert('Deleted'); location.reload();
  };
});

function escapeHtml(s){ return (s||'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;'); }

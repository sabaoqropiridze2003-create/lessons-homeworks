const API_URL = 'https://jsonplaceholder.typicode.com/todos';
const ITEMS_PER_PAGE = 10;

const state = {
  todos: [],
  filteredTodos: [],
  currentPage: 1,
  searchTerm: '',
  userFilter: 'all',
  completedFilter: 'all',
  selectedTodoId: null,
};

const elements = {
  loading: document.getElementById('loading'),
  todosPage: document.getElementById('todos-page'),
  detailPage: document.getElementById('todo-detail-page'),
  errorPage: document.getElementById('error-page'),
  searchInput: document.getElementById('search-input'),
  userFilter: document.getElementById('user-filter'),
  completedFilter: document.getElementById('completed-filter'),
  todosList: document.getElementById('todos-list'),
  pagination: document.getElementById('pagination'),
  resultsSummary: document.getElementById('results-summary'),
  backButton: document.getElementById('back-button'),
  detailTitle: document.getElementById('detail-title'),
  detailUserId: document.getElementById('detail-userId'),
  detailId: document.getElementById('detail-id'),
  detailBody: document.getElementById('detail-body'),
  detailCompleted: document.getElementById('detail-completed'),
  retryButton: document.getElementById('retry-button'),
};

function showPage(page) {
  [elements.loading, elements.todosPage, elements.detailPage, elements.errorPage].forEach((section) => {
    section.classList.add('hidden');
  });

  page.classList.remove('hidden');
}

function buildUserOptions() {
  const uniqueUsers = [...new Set(state.todos.map((todo) => todo.userId))].sort((a, b) => a - b);
  elements.userFilter.innerHTML = '<option value="all">All users</option>' + uniqueUsers
    .map((userId) => `<option value="${userId}">User ${userId}</option>`)
    .join('');
}

function parseFilters() {
  const searchTerm = state.searchTerm.trim().toLowerCase();
  const userFilter = state.userFilter;
  const completedFilter = state.completedFilter;

  state.filteredTodos = state.todos.filter((todo) => {
    const matchesSearch = !searchTerm || todo.title.toLowerCase().includes(searchTerm);
    const matchesUser = userFilter === 'all' || String(todo.userId) === userFilter;
    const matchesCompleted =
      completedFilter === 'all' || String(todo.completed) === completedFilter;

    return matchesSearch && matchesUser && matchesCompleted;
  });
}

function renderTodos() {
  parseFilters();

  const total = state.filteredTodos.length;
  const pageCount = Math.max(1, Math.ceil(total / ITEMS_PER_PAGE));
  state.currentPage = Math.min(state.currentPage, pageCount);

  const startIndex = (state.currentPage - 1) * ITEMS_PER_PAGE;
  const pageTodos = state.filteredTodos.slice(startIndex, startIndex + ITEMS_PER_PAGE);

  elements.resultsSummary.textContent = `Showing ${pageTodos.length} of ${total} todos`;

  if (!total) {
    elements.todosList.innerHTML = '<li class="todo-item"><p>No todos match your criteria.</p></li>';
    elements.pagination.innerHTML = '';
    return;
  }

  elements.todosList.innerHTML = pageTodos
    .map(
      (todo) => `
      <li class="todo-item">
        <a href="#/todo/${todo.id}" class="todo-link">${escapeHtml(todo.title)}</a>
        <p class="todo-meta">User ${todo.userId} · ${todo.completed ? 'Completed' : 'Pending'}</p>
      </li>
    `
    )
    .join('');

  renderPagination(pageCount);
}

function renderPagination(pageCount) {
  const controls = [];

  const prevDisabled = state.currentPage <= 1;
  const nextDisabled = state.currentPage >= pageCount;

  controls.push(
    `<button class="page-button" data-page="${state.currentPage - 1}" ${prevDisabled ? 'disabled' : ''}>Previous</button>`
  );

  for (let page = 1; page <= pageCount; page += 1) {
    controls.push(
      `<button class="page-button ${page === state.currentPage ? 'active' : ''}" data-page="${page}">${page}</button>`
    );
  }

  controls.push(
    `<button class="page-button" data-page="${state.currentPage + 1}" ${nextDisabled ? 'disabled' : ''}>Next</button>`
  );

  elements.pagination.innerHTML = controls.join('');
}

function renderTodoDetail(todoId) {
  const todo = state.todos.find((item) => String(item.id) === String(todoId));
  if (!todo) {
    elements.detailTitle.textContent = 'Todo not found';
    elements.detailUserId.textContent = '-';
    elements.detailId.textContent = '-';
    elements.detailBody.textContent = '-';
    elements.detailCompleted.textContent = '-';
    showPage(elements.detailPage);
    return;
  }

  elements.detailTitle.textContent = todo.title;
  elements.detailUserId.textContent = todo.userId;
  elements.detailId.textContent = todo.id;
  elements.detailBody.textContent = todo.title;
  elements.detailCompleted.textContent = todo.completed ? 'Yes' : 'No';
  showPage(elements.detailPage);
}

function escapeHtml(value) {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function updateHashFromState() {
  const hashParts = ['#/todos'];
  const params = new URLSearchParams();

  if (state.searchTerm) params.set('search', state.searchTerm);
  if (state.userFilter !== 'all') params.set('user', state.userFilter);
  if (state.completedFilter !== 'all') params.set('completed', state.completedFilter);
  if (state.currentPage > 1) params.set('page', String(state.currentPage));

  const queryString = params.toString();
  const newHash = queryString ? `${hashParts[0]}?${queryString}` : hashParts[0];

  if (location.hash !== newHash) {
    history.replaceState(null, '', newHash);
  }
}

function applyQueryState() {
  const hash = location.hash || '#/todos';
  const [path, queryString = ''] = hash.split('?');
  const params = new URLSearchParams(queryString);
  const search = params.get('search') || '';
  const user = params.get('user') || 'all';
  const completed = params.get('completed') || 'all';
  const page = Number(params.get('page')) || 1;

  state.searchTerm = search;
  state.userFilter = user;
  state.completedFilter = completed;
  state.currentPage = page;

  elements.searchInput.value = state.searchTerm;
  elements.userFilter.value = state.userFilter;
  elements.completedFilter.value = state.completedFilter;
}

function route() {
  const hash = location.hash || '#/todos';
  const [path, queryString] = hash.split('?');

  if (path.startsWith('#/todo/')) {
    const todoId = path.replace('#/todo/', '');
    renderTodoDetail(todoId);
    return;
  }

  if (path === '#/todos' || path === '#/') {
    applyQueryState();
    renderTodos();
    showPage(elements.todosPage);
    updateHashFromState();
    return;
  }

  location.hash = '#/todos';
}

async function loadTodos() {
  showPage(elements.loading);
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error('Failed to fetch todos');
    }

    state.todos = await response.json();
    buildUserOptions();
    elements.searchInput.value = state.searchTerm;
    elements.userFilter.value = state.userFilter;
    elements.completedFilter.value = state.completedFilter;
    route();
  } catch (error) {
    console.error(error);
    showPage(elements.errorPage);
  }
}

function bindEvents() {
  elements.searchInput.addEventListener('input', (event) => {
    state.searchTerm = event.target.value;
    state.currentPage = 1;
    renderTodos();
    updateHashFromState();
  });

  elements.userFilter.addEventListener('change', (event) => {
    state.userFilter = event.target.value;
    state.currentPage = 1;
    renderTodos();
    updateHashFromState();
  });

  elements.completedFilter.addEventListener('change', (event) => {
    state.completedFilter = event.target.value;
    state.currentPage = 1;
    renderTodos();
    updateHashFromState();
  });

  elements.pagination.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.disabled) return;

    state.currentPage = Number(button.dataset.page);
    renderTodos();
    updateHashFromState();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  elements.backButton.addEventListener('click', () => {
    location.hash = '#/todos';
  });

  elements.retryButton.addEventListener('click', loadTodos);

  window.addEventListener('hashchange', route);
}

function init() {
  bindEvents();
  loadTodos();
}

init();

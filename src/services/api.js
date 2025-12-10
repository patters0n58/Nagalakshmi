export async function fetchItems(apiBase) {
  const res = await fetch(apiBase);
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt || "Failed to fetch items");
  }
  return res.json();
}

export async function createItem(apiBase, item) {
  const res = await fetch(apiBase, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item)
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt || "Failed to create item");
  }
  return res.json();
}

export async function updateItem(apiBase, id, item) {
  const res = await fetch(`${apiBase}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item)
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt || "Failed to update item");
  }
  return res.json();
}

export async function deleteItem(apiBase, id) {
  const res = await fetch(`${apiBase}/${id}`, {
    method: "DELETE"
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt || "Failed to delete item");
  }
  return res.json();
}

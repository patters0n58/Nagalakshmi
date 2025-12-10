import React, { useEffect, useState } from "react";
import ItemForm from "../shared/ItemForm";
import ItemTable from "../shared/ItemTable";
import { fetchItems, createItem, updateItem, deleteItem } from "../services/api";


const API_BASE = process.env.REACT_APP_API_URL || "http://138.68.140.83:4000/api/items";

export default function ItemsPage() {
  const [items, setItems] = useState([]);
  const [message, setMessage] = useState(null); // { text, type }
  const [editItem, setEditItem] = useState(null);

  async function load() {
    try {
      const data = await fetchItems(API_BASE);
      setItems(data || []);
      if (!data || data.length === 0) {
        showMessage("No items found in database", "error");
      }
    } catch (err) {
      showMessage("Error loading items: " + (err.message || err), "error");
    }
  }

  useEffect(() => {
    load();
  }, []);

  function showMessage(text, type = "success") {
    setMessage({ text, type });
    setTimeout(() => setMessage(null), 3000);
  }

  async function handleSave(item) {
    try {
      if (editItem) {
        await updateItem(API_BASE, editItem.ItemID, item);
        showMessage("Item updated successfully", "success");
      } else {
        await createItem(API_BASE, item);
        showMessage("Item created successfully", "success");
      }
      setEditItem(null);
      await load();
    } catch (err) {
      showMessage("Error saving item: " + (err.message || err), "error");
    }
  }

  async function handleDelete(itemId) {
    if (!window.confirm(`Are you sure you want to delete item ${itemId}?`)) return;
    try {
      await deleteItem(API_BASE, itemId);
      showMessage("Item deleted successfully", "success");
      await load();
    } catch (err) {
      showMessage("Error deleting item: " + (err.message || err), "error");
    }
  }

  function handleEdit(item) {
    setEditItem(item);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function handleCancelEdit() {
    setEditItem(null);
  }

  return (
    <div className="container">
      <h1>Item Management</h1>

      <div className="form-container">
        {message && <div className={`message ${message.type}`}>{message.text}</div>}
        <ItemForm onSave={handleSave} editItem={editItem} onCancel={handleCancelEdit} />
      </div>

      <div className="table-container">
        <h2>Item Details</h2>
        <ItemTable items={items} onEdit={handleEdit} onDelete={handleDelete} />
      </div>
    </div>
  );
}

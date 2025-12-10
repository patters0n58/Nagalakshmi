import React, { useEffect, useState } from "react";

export default function ItemForm({ onSave, editItem, onCancel }) {
  const [item, setItem] = useState({
    ItemID: "",
    Description: "",
    UnitPrice: "",
    StockQty: "",
    SupplierID: ""
  });

  useEffect(() => {
    if (editItem) {
      setItem({
        ItemID: editItem.ItemID,
        Description: editItem.Description,
        UnitPrice: editItem.UnitPrice,
        StockQty: editItem.StockQty,
        SupplierID: editItem.SupplierID
      });
    } else {
      setItem({
        ItemID: "",
        Description: "",
        UnitPrice: "",
        StockQty: "",
        SupplierID: ""
      });
    }
  }, [editItem]);

  function updateField(e) {
    const { name, value } = e.target;
    setItem(prev => ({ ...prev, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (!item.ItemID || !item.Description) {
      alert("Please fill in Item ID and Description");
      return;
    }
    const payload = {
      ItemID: item.ItemID,
      Description: item.Description,
      UnitPrice: parseFloat(item.UnitPrice) || 0,
      StockQty: parseInt(item.StockQty, 10) || 0,
      SupplierID: item.SupplierID
    };
    onSave(payload);
  }

  return (
    <form className="form-row" onSubmit={handleSubmit}>
      <input
        name="ItemID"
        type="text"
        placeholder="Enter Item Id"
        value={item.ItemID}
        onChange={updateField}
        disabled={!!editItem}
      />
      <input
        name="Description"
        type="text"
        placeholder="Enter Description"
        value={item.Description}
        onChange={updateField}
      />
      <input
        name="UnitPrice"
        type="number"
        placeholder="Enter Unit Price"
        value={item.UnitPrice}
        onChange={updateField}
      />
      <input
        name="StockQty"
        type="number"
        placeholder="Enter Stock Quantity"
        value={item.StockQty}
        onChange={updateField}
      />
      <input
        name="SupplierID"
        type="text"
        placeholder="Enter Supplier Id"
        value={item.SupplierID}
        onChange={updateField}
      />
      <div style={{ display: "flex", gap: 8 }}>
        <button type="submit">{editItem ? "Update Item" : "Save Item"}</button>
        {editItem && <button type="button" onClick={onCancel}>Cancel</button>}
      </div>
    </form>
  );
}

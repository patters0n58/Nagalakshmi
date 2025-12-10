import React from "react";

export default function ItemTable({ items = [], onEdit, onDelete }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Item Id</th>
          <th>Description</th>
          <th>Unit Price</th>
          <th>Stock Quantity</th>
          <th>Supplier Id</th>
          <th>Update</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        {items.map(item => (
          <tr key={item.ItemID}>
            <td>{item.ItemID}</td>
            <td>{item.Description}</td>
            <td>{item.UnitPrice}</td>
            <td>{item.StockQty}</td>
            <td>{item.SupplierID}</td>
            <td>
              <button className="action-btn update-btn" onClick={() => onEdit(item)}>✏️</button>
            </td>
            <td>
              <button className="action-btn delete-btn" onClick={() => onDelete(item.ItemID)}>🗑️</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

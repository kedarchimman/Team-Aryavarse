<template>
  <div>
    <div class="bg-yellow-100 p-3 mb-4 rounded">
      ⚠ Low Stock Alert - 4 products below minimum
    </div>

    <table class="w-full bg-white rounded shadow">
      <tr class="border-b">
        <th>Product</th>
        <th>Current</th>
        <th>Min</th>
      </tr>

      <tr class="bg-yellow-50">
        <td>Medical Cap</td>
        <td>5</td>
        <td>10</td>
      </tr>

      <tr class="bg-red-50">
        <td>Nurse Uniform</td>
        <td>0</td>
        <td>10</td>
      </tr>
    </table>
  </div>
</template>
let data = [
  {
    id: 1,
    name: "Tomato",
    name_ml: "തക്കാളി",
    type: "vegetable",
    price: 40,
    image: "🍅",
    updated_at: null
  },
  {
    id: 2,
    name: "Potato",
    name_ml: "ഉരുളക്കിഴങ്ങ്",
    type: "vegetable",
    price: 30,
    image: "🥔",
    updated_at: null
  },
  {
    id: 3,
    name: "Onion",
    name_ml: "സവാള",
    type: "vegetable",
    price: 35,
    image: "🧅",
    updated_at: null
  },
  {
    id: 4,
    name: "Carrot",
    name_ml: "കാരറ്റ്",
    type: "vegetable",
    price: 50,
    image: "🥕",
    updated_at: null
  },
  {
    id: 5,
    name: "Cabbage",
    name_ml: "കാബേജ്",
    type: "vegetable",
    price: 25,
    image: "🥬",
    updated_at: null
  },
  {
    id: 6,
    name: "Banana",
    name_ml: "വാഴപ്പഴം",
    type: "fruit",
    price: 50,
    image: "🍌",
    updated_at: null
  },
  {
    id: 7,
    name: "Mango",
    name_ml: "മാങ്ങ",
    type: "fruit",
    price: 120,
    image: "🥭",
    updated_at: null
  }
];

export default function handler(req, res) {
  // GET
  if (req.method === "GET") {
    return res.status(200).json({
      status: "success",
      count: data.length,
      data
    });
  }

  // PUT (update price + time)
  if (req.method === "PUT") {
    const { id, price } = req.body;

    const index = data.findIndex(item => item.id === id);

    if (index === -1) {
      return res.status(404).json({ message: "Item not found" });
    }

    data[index].price = price;
    data[index].updated_at = new Date().toISOString();

    return res.status(200).json({
      status: "updated",
      data: data[index]
    });
  }

  res.status(405).json({ message: "Method not allowed" });
    }

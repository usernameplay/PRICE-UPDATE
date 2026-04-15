// pages/api/items.js

// 82 ഐറ്റങ്ങളും ഉൾപ്പെടുത്തിയ ലിസ്റ്റ്
let itemsList = [
    {"id":1,"name":"Tomato","name_ml":"തക്കാളി","type":"vegetable","price":40,"image":"🍅","updated_at":null},
    {"id":2,"name":"Potato","name_ml":"ഉരുളക്കിഴങ്ങ്","type":"vegetable","price":30,"image":"🥔","updated_at":null},
    {"id":3,"name":"Onion","name_ml":"സവാള","type":"vegetable","price":35,"image":"🧅","updated_at":null},
    {"id":4,"name":"Carrot","name_ml":"കാരറ്റ്","type":"vegetable","price":50,"image":"🥕","updated_at":null},
    {"id":5,"name":"Cabbage","name_ml":"കാബേജ്","type":"vegetable","price":25,"image":"🥬","updated_at":null},
    {"id":6,"name":"Banana","name_ml":"വാഴപ്പഴം","type":"fruit","price":50,"image":"🍌","updated_at":null},
    {"id":7,"name":"Mango","name_ml":"മാങ്ങ","type":"fruit","price":500,"image":"🥭","updated_at":null},
    {"id":8,"name":"Brinjal","name_ml":"വഴുതന","type":"vegetable","price":45,"image":"🍆","updated_at":null},
    {"id":9,"name":"Beans","name_ml":"ബീൻസ്","type":"vegetable","price":60,"image":"🫘","updated_at":null},
    {"id":10,"name":"Apple","name_ml":"ആപ്പിൾ","type":"fruit","price":180,"image":"🍎","updated_at":null},
    {"id":11,"name":"Orange","name_ml":"ഓറഞ്ച്","type":"fruit","price":120,"image":"🍊","updated_at":null},
    {"id":12,"name":"Pineapple","name_ml":"കൈതച്ചക്ക","type":"fruit","price":90,"image":"🍍","updated_at":null},
    {"id":13,"name":"Papaya","name_ml":"പപ്പായ","type":"fruit","price":60,"image":"🥭","updated_at":null},
    {"id":14,"name":"Watermelon","name_ml":"തണ്ണിമത്തൻ","type":"fruit","price":30,"image":"🍉","updated_at":null},
    {"id":15,"name":"Grapes","name_ml":"മുന്തിരി","type":"fruit","price":90,"image":"🍇","updated_at":null},
    {"id":16,"name":"Guava","name_ml":"പേരയ്ക്ക","type":"fruit","price":70,"image":"🍏","updated_at":null},
    {"id":17,"name":"Chili","name_ml":"മുളക്","type":"vegetable","price":80,"image":"🌶️","updated_at":null},
    {"id":18,"name":"Cucumber","name_ml":"വെള്ളരി","type":"vegetable","price":35,"image":"🥒","updated_at":null},
    {"id":19,"name":"Drumstick","name_ml":"മുരിങ്ങക്കായ്","type":"vegetable","price":70,"image":"🥬","updated_at":null},
    {"id":20,"name":"Pumpkin","name_ml":"മത്തങ്ങ","type":"vegetable","price":40,"image":"🎃","updated_at":null},
    {"id":21,"name":"Bitter Gourd","name_ml":"പാവയ്ക്ക","type":"vegetable","price":60,"image":"🥒","updated_at":null},
    {"id":22,"name":"Snake Gourd","name_ml":"പടവലങ്ങ","type":"vegetable","price":50,"image":"🥒","updated_at":null},
    {"id":23,"name":"Ash Gourd","name_ml":"കുമ്പളങ്ങ","type":"vegetable","price":30,"image":"🥒","updated_at":null},
    {"id":24,"name":"Ladies Finger","name_ml":"വെണ്ടക്ക","type":"vegetable","price":55,"image":"🥬","updated_at":null},
    {"id":25,"name":"Beetroot","name_ml":"ബീറ്റ്റൂട്ട്","type":"vegetable","price":45,"image":"🥕","updated_at":null},
    {"id":26,"name":"Radish","name_ml":"മുള്ളങ്കി","type":"vegetable","price":30,"image":"🥕","updated_at":null},
    {"id":27,"name":"Spinach","name_ml":"ചീര","type":"vegetable","price":20,"image":"🥬","updated_at":null},
    {"id":28,"name":"Mint","name_ml":"പുതിന","type":"vegetable","price":15,"image":"🌿","updated_at":null},
    {"id":29,"name":"Coriander","name_ml":"മല്ലിയില","type":"vegetable","price":15,"image":"🌿","updated_at":null},
    {"id":30,"name":"Garlic","name_ml":"വെളുത്തുള്ളി","type":"vegetable","price":120,"image":"🧄","updated_at":null},
    {"id":31,"name":"Ginger","name_ml":"ഇഞ്ചി","type":"vegetable","price":100,"image":"🫚","updated_at":null},
    {"id":32,"name":"Sweet Potato","name_ml":"മധുരക്കിഴങ്ങ്","type":"vegetable","price":40,"image":"🍠","updated_at":null},
    {"id":33,"name":"Tapioca","name_ml":"കപ്പ","type":"vegetable","price":25,"image":"🍠","updated_at":null},
    {"id":34,"name":"Green Peas","name_ml":"പട്ടാണി","type":"vegetable","price":90,"image":"🫘","updated_at":null},
    {"id":35,"name":"Corn","name_ml":"മക്കച്ചോലം","type":"vegetable","price":40,"image":"🌽","updated_at":null},
    {"id":36,"name":"Capsicum","name_ml":"കാപ്സിക്കം","type":"vegetable","price":80,"image":"🫑","updated_at":null},
    {"id":37,"name":"Mushroom","name_ml":"കൂൺ","type":"vegetable","price":120,"image":"🍄","updated_at":null},
    {"id":38,"name":"Zucchini","name_ml":"സുക്കിനി","type":"vegetable","price":90,"image":"🥒","updated_at":null},
    {"id":39,"name":"Broccoli","name_ml":"ബ്രോക്കോളി","type":"vegetable","price":120,"image":"🥦","updated_at":null},
    {"id":40,"name":"Cauliflower","name_ml":"കോവൽഫ്ലവർ","type":"vegetable","price":60,"image":"🥦","updated_at":null},
    {"id":41,"name":"Pear","name_ml":"പെയർ","type":"fruit","price":150,"image":"🍐","updated_at":null},
    {"id":42,"name":"Pomegranate","name_ml":"മാതളനാരങ്ങ","type":"fruit","price":160,"image":"🍎","updated_at":null},
    {"id":43,"name":"Kiwi","name_ml":"കിവി","type":"fruit","price":200,"image":"🥝","updated_at":null},
    {"id":44,"name":"Strawberry","name_ml":"സ്ട്രോബെറി","type":"fruit","price":250,"image":"🍓","updated_at":null},
    {"id":45,"name":"Blueberry","name_ml":"ബ്ലൂബെറി","type":"fruit","price":300,"image":"🫐","updated_at":null},
    {"id":46,"name":"Cherry","name_ml":"ചെറി","type":"fruit","price":280,"image":"🍒","updated_at":null},
    {"id":47,"name":"Plum","name_ml":"പ്ലം","type":"fruit","price":220,"image":"🍑","updated_at":null},
    {"id":48,"name":"Peach","name_ml":"പീച്ച്","type":"fruit","price":240,"image":"🍑","updated_at":null},
    {"id":49,"name":"Apricot","name_ml":"ആപ്രിക്കോട്ട്","type":"fruit","price":260,"image":"🍑","updated_at":null},
    {"id":50,"name":"Dragon Fruit","name_ml":"ഡ്രാഗൺ ഫ്രൂട്ട്","type":"fruit","price":180,"image":"🍉","updated_at":null},
    {"id":51,"name":"Jackfruit","name_ml":"ചക്ക","type":"fruit","price":100,"image":"🍈","updated_at":null},
    {"id":52,"name":"Custard Apple","name_ml":"സീതപ്പഴം","type":"fruit","price":120,"image":"🍏","updated_at":null},
    {"id":53,"name":"Sapota","name_ml":"ചിക്കു","type":"fruit","price":80,"image":"🍏","updated_at":null},
    {"id":54,"name":"Fig","name_ml":"അത്തി","type":"fruit","price":300,"image":"🍑","updated_at":null},
    {"id":55,"name":"Dates","name_ml":"ഖജൂർ","type":"fruit","price":220,"image":"🍇","updated_at":null},
    {"id":56,"name":"Lychee","name_ml":"ലിച്ചി","type":"fruit","price":250,"image":"🍒","updated_at":null},
    {"id":57,"name":"Avocado","name_ml":"അവക്കാഡോ","type":"fruit","price":200,"image":"🥑","updated_at":null},
    {"id":58,"name":"Star Fruit","name_ml":"കമരങ്ങ","type":"fruit","price":90,"image":"⭐","updated_at":null},
    {"id":59,"name":"Wood Apple","name_ml":"കബളങ്ങ","type":"fruit","price":70,"image":"🍏","updated_at":null},
    {"id":60,"name":"Lemon","name_ml":"നാരങ്ങ","type":"fruit","price":60,"image":"🍋","updated_at":null},
    {"id":61,"name":"Butter Fruit","name_ml":"ബട്ടർ ഫ്രൂട്ട്","type":"fruit","price":180,"image":"🥑","updated_at":null},
    {"id":62,"name":"Long Beans","name_ml":"പയർ","type":"vegetable","price":50,"image":"🫘","updated_at":null},
    {"id":63,"name":"Ivy Gourd","name_ml":"കോവയ്ക്ക","type":"vegetable","price":45,"image":"🥒","updated_at":null},
    {"id":64,"name":"Ridge Gourd","name_ml":"പീച്ചിങ്ങ","type":"vegetable","price":40,"image":"🥒","updated_at":null},
    {"id":65,"name":"Cluster Beans","name_ml":"ഗ്വാർ","type":"vegetable","price":55,"image":"🫘","updated_at":null},
    {"id":66,"name":"Turnip","name_ml":"ഷൽഗം","type":"vegetable","price":35,"image":"🥕","updated_at":null},
    {"id":67,"name":"Leek","name_ml":"ലീക്ക്","type":"vegetable","price":70,"image":"🥬","updated_at":null},
    {"id":68,"name":"Spring Onion","name_ml":"ഇലസവാള","type":"vegetable","price":40,"image":"🧅","updated_at":null},
    {"id":69,"name":"Red Cabbage","name_ml":"ചുവന്ന കാബേജ്","type":"vegetable","price":60,"image":"🥬","updated_at":null},
    {"id":70,"name":"Yellow Capsicum","name_ml":"മഞ്ഞ കാപ്സിക്കം","type":"vegetable","price":90,"image":"🫑","updated_at":null},
    {"id":71,"name":"Red Capsicum","name_ml":"ചുവന്ന കാപ്സിക്കം","type":"vegetable","price":90,"image":"🫑","updated_at":null},
    {"id":72,"name":"Green Apple","name_ml":"പച്ച ആപ്പിൾ","type":"fruit","price":180,"image":"🍏","updated_at":null},
    {"id":73,"name":"Black Grapes","name_ml":"കറുത്ത മുന്തിരി","type":"fruit","price":100,"image":"🍇","updated_at":null},
    {"id":74,"name":"Tender Coconut","name_ml":"തേങ്ങാവെള്ളം","type":"fruit","price":40,"image":"🥥","updated_at":null},
    {"id":75,"name":"Dry Coconut","name_ml":"തേങ്ങ","type":"fruit","price":35,"image":"🥥","updated_at":null},
    {"id":76,"name":"Gooseberry","name_ml":"നെല്ലിക്ക","type":"fruit","price":80,"image":"🟢","updated_at":null},
    {"id":77,"name":"Jamun","name_ml":"ഞാവൽപ്പഴം","type":"fruit","price":120,"image":"🟣","updated_at":null},
    {"id":78,"name":"Mulberry","name_ml":"മുള്ബെറി","type":"fruit","price":150,"image":"🍇","updated_at":null},
    {"id":79,"name":"Breadfruit","name_ml":"കദളക്ക","type":"fruit","price":60,"image":"🍈","updated_at":null},
    {"id":80,"name":"Raw Mango","name_ml":"പച്ച മാങ്ങ","type":"fruit","price":80,"image":"🥭","updated_at":null},
    {"id":81,"name":"Elephant Yam","name_ml":"ചേന","type":"vegetable","price":70,"image":"🍠","updated_at":null},
    {"id":82,"name":"Colocasia","name_ml":"ചേമ്പ്","type":"vegetable","price":60,"image":"🍠","updated_at":null}
];

export default function handler(req, res) {
  // GET: എല്ലാ ഡാറ്റയും അയക്കുന്നു
  if (req.method === "GET") {
    return res.status(200).json({
      status: "success",
      count: itemsList.length,
      data: itemsList
    });
  }

  // PUT: വിലയും പുതുക്കിയ സമയവും സേവ് ചെയ്യുന്നു
  if (req.method === "PUT") {
    const { id, price } = req.body;

    // ഐറ്റത്തിന്റെ ഇൻഡക്സ് കണ്ടെത്തുന്നു
    const index = itemsList.findIndex(item => item.id === Number(id));

    if (index === -1) {
      return res.status(404).json({ message: "Item not found" });
    }

    // വിലയും സമയവും അപ്‌ഡേറ്റ് ചെയ്യുന്നു
    itemsList[index].price = Number(price);
    itemsList[index].updated_at = new Date().toISOString();

    return res.status(200).json({
      status: "updated",
      data: itemsList[index]
    });
  }

  // മറ്റേതെങ്കിലും മെത്തേഡ് വന്നാൽ
  res.status(405).json({ message: "Method not allowed" });
  }
      

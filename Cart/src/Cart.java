import java.util.HashMap;
import java.util.Map;


public class Cart {
	private Map<String, Integer> cart = new HashMap<String, Integer>();
	
	public void addProduct(String productCode, int quantity) {
		if (!cart.containsKey(productCode)) 
			cart.put(productCode, quantity);
		else
			cart.put(productCode, cart.get(productCode) + quantity);
	}
	
	
	public void removeProduct(String productCode) {
		if (cart.containsKey(productCode))
			cart.remove(productCode);
	}
	
	public void showCart() {
		for (Map.Entry<String, Integer> item : cart.entrySet()) {
			System.out.println(item.getKey() + " " + "(" + item.getValue() + ")");
		}
	}
	
	public Map<String, Integer> getCart() {
		return cart;
	}
}

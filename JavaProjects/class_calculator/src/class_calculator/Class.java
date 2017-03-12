/**
 * 
 */
package class_calculator;

/**
 * @author anish
 *
 */
public class Class {

	private boolean isWeighted;
	private String instructor;
	private String className;
	
	
	
	public Class(){
		
		isWeighted = true;
		instructor = " ";
		className = " ";
		
	}
	public Class (String name, String teacher, boolean weighted){
		className = name;
		instructor = teacher;
		isWeighted = weighted;
		
	}
	
	public String get_className(){
		return className;
	}
	public boolean get_isWeighted(){
		return isWeighted;
	}
	public String get_instructor(){
		return instructor;
	}
	
	
	
	public void set_className(String name){
		className = name;
	}
	public void set_isWeighted(boolean weighted){
		isWeighted = weighted;
	}
	public void set_instructor(String teacher){
		instructor = teacher;
	}	
	
	
	
	
	
	
	
	
	
}

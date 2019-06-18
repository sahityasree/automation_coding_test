/*Write a selenium script that prints the html tag of all the links ( tags) on the website http://www.inmar.com */
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;

public class tags {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//ff
		System.setProperty("webdriver.gecko.driver","C://Users/Admin/Desktop/sahitya/projects/selenium/geckodriver-v0.23.0-win64/geckodriver.exe");
		WebDriver driver= new FirefoxDriver();
		driver.get("http://www.inmar.com");
		/*String str=driver.getTitle();
		 * 
		#System.out.println(str);*/
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS) ;
		List<WebElement> links = driver.findElements(By.tagName("a"));
		System.out.println(links.size());		 
		for (int i = 1; i<=links.size()-1; i=i+1)
		{
			System.out.println(links.get(i).getText());
		}
		driver.close();
		
	}
	

}

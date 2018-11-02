/*Write a Selenium script that clicks the button “New Browser tab” on the form http://www.seleniumframework.com/Practiceform/ and prints
the title of the page that opens in the new tab. Also verify that two windows are open and print the title of both the windows
*/
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriver.TargetLocator;
import org.openqa.selenium.firefox.FirefoxDriver;

public class selenium_newbrowsertab {
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.gecko.driver","C://Users/Admin/Desktop/sahitya/projects/selenium/geckodriver-v0.23.0-win64/geckodriver.exe");
		WebDriver driver= new FirefoxDriver();
		driver.get("http://www.seleniumframework.com/Practiceform/");
		
		String parenthandle=driver.getWindowHandle();
		System.out.println("parent handle is " +parenthandle);
		String str=driver.getTitle();
		System.out.println("the title before button: " +str);
		String label = "New Browser tab";
		driver.findElement(By.xpath("//button[contains(.,label)]")).click();
		//driver.findElement(By.xpath("//button[contains(.,label)]")).click();
		System.out.println("page is navigated");
		Set<String> handles=driver.getWindowHandles();
		//System.out.println("the titles after button clicked");
		
		for(String handle : handles)
		{	System.out.println("browser handle is: " +handle);
			//System.out.println(handle);
			driver.switchTo().window(handle);
			driver.manage().window().maximize();
			driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS) ;
			String str3=driver.getTitle();
			System.out.println("title is: " +str3);
			
		}
		
			driver.close();
			driver.switchTo().window(parenthandle);
			driver.close();
}
}

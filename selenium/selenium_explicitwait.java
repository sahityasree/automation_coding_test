
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class exwait {

	public static void main(String[] args) {
		
		/*
		 *It is more extendible in the means that you can set it up to wait 
		 for any condition you might like.
		 * Usually, you can use some of the prebuilt ExpectedConditions to wait for 
		 elements to become clickable, visible, invisible, etc.
		 */
		System.setProperty("webdriver.gecko.driver","C://Users/Admin/Desktop/sahitya/projects/selenium/geckodriver-v0.23.0-win64/geckodriver.exe");
		WebDriver driver= new FirefoxDriver();
		//WebDriverWait wait=new WebDriverWait(driver, 20);
		//driver.manage().timeouts().implicitlyWait(60,TimeUnit.SECONDS) ;
		String eTitle = "Advanced Technology and Data Analytics for Intelligent Commerce - Inmar";
	    String actualTitle = "" ;
	    
		driver.get("https://www.inmar.com/" );
		List<WebElement> links=driver.findElements(By.tagName("a"));
		WebDriverWait wait = new WebDriverWait(driver,60);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(),'Connect on LinkedIn')]")));
		driver.findElement(By.xpath("//*[contains(text(),'Connect on LinkedIn')]")).click();
		driver.close();
	}

	
}

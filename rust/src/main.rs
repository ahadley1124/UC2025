use rppal::i2c::I2c;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Hello, world!");
    let i2c = I2c::new()?;
    println!("{:#?}", i2c);
    Ok(())
}

namespace Behavior
{
    // You can have many way to quack: sqeak, nothing (like a wooden duck)
    public interface IQuackBehavior
    {
        public void Quack();
    }

    public class Quack : IQuackBehavior
    {
        public void Quack()
        {
            Console.WriteLine("Quacking...");
        }
    }

    public class Squeak : IQuackBehavior
    {
        public void Quack()
        {
            Console.WriteLine("Squeaking like a rubber duck...");
        }
    }

    public class Scream : IQuackBehavior
    {
        public void Quack()
        {
            Console.WriteLine("AAAAAAAAAA...");
        }
    }
}
namespace Behavior
{
    // You can have many way to fly: flap your wing, using jet engine
    public interface IFlyBehavior : IBehavior
    {
        public void Fly();
    }

    public class FlyWithWings : IFlyBehavior
    {
        public void Fly ()
        {
            Console.WriteLine("Flapping");
        }
    }

    public class FlyByEngine : IFlyBehavior
    {
        public void Fly ()
        {
            Console.WriteLine("Starting engine...");
        }
    }
}
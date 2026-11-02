using Animal;
using Behaviors;

namespace StrategyPattern
{
    public void Main()
    {
        var duck = new Duck(new FlyWithEngine(), new Scream());
        duck.Action();
        duck.MakeSound();
    }
}